import argparse
from glob import glob

from fpga.project import Project

parser = argparse.ArgumentParser()
parser.add_argument(
    '--tool',
    '-t',
    default='ise'
)
args = parser.parse_args()

verilogs = glob('temp/**/*.v', recursive=True)
filesqty = len(verilogs)

print('* Collected Verilog files: %s' % filesqty)

fh = open('{}.log'.format(args.tool), 'w')
fileno = 1

for filename in verilogs:
    info = '* {} - {} ({}/{})'.format(args.tool, filename, fileno, filesqty)
    print(info)
    PRJ = Project(args.tool)
    dirname = filename.replace('/', '_').replace('.v', '')
    PRJ.set_outdir('build/{}'.format(dirname))
    PRJ.add_files(filename)
    PRJ.set_top(filename)
    try:
        PRJ.generate(to_task='syn')
    except Exception as e:
        fh.write(info + '\n\n')
        fh.write('{} ({})\n\n'.format(type(e).__name__, e))
    fileno += 1
