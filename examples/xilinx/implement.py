import argparse
import os
from glob import glob

from fpga.project import Project

parser = argparse.ArgumentParser()
parser.add_argument(
    '--tool',
    '-t',
    default='ise'
)
args = parser.parse_args()
tool = args.tool

files = glob('temp/ise/**/*.v', recursive=True)
files.extend(glob('temp/vivado/**/*.v', recursive=True))
filesqty = len(files)

print('* Collected Verilog files: %s' % filesqty)
print('* Tool to be used: %s' % tool)

fileno = 1
for filename in files:
    basename = os.path.basename(filename)
    basename = os.path.splitext(basename)[0]
    pathname = os.path.dirname(filename)
    #
    print('* {} ({}/{})'.format(filename, fileno, filesqty))
    PRJ = Project(tool)
    PRJ.set_outdir('build/{}/{}'.format(tool, basename))
    if basename in ['EvenSymTranspConvFIR', 'OddSymTranspConvFIR']:
        PRJ.add_files(os.path.join(pathname, '/DelayLine.v'))
        PRJ.add_files(os.path.join(pathname, '/FilterStage.v'))
    PRJ.add_files(filename)
    PRJ.set_top(filename)
    try:
        output = PRJ.generate(to_task='imp', capture=True)
        open('build/{}/{}.txt'.format(tool, basename), 'w').write(
            '#### STDOUT:\n'
            + output.stdout + '\n' +
            '#### STDERR:\n'
            + output.stderr
        )
    except Exception as e:
        print('FAILED:\n')
        print('{} ({})\n\n'.format(type(e).__name__, e))
    fileno += 1
