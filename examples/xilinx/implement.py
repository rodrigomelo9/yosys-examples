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

unsupported = [
    # 'assign' is not a supported statement for synthesis
    'assign_deassign_reject_1',
    'assign_deassign_reject_2',
    'assign_deassign_reject_3',
    # Supposed to work, but fails
    'assign_deassign_good'
]

vivado_unsupported = [
    # [Synth 8-2914] Unsupported RAM template
    'asymmetric_ram_3',
    # [Synth 8-2913] Unsupported Dual Port Block-RAM template for RAM_reg
    'asymmetric_write_first_1',
    'asymmetric_write_first_2',
    'asymmetric_write_first_3',
    'asymmetric_ram_2d',
    'asymmetric_ram_2c',
    'asymmetric_ram_4',
    # [Synth 8-27] primitive not supported
    'udp_sequential_1',
    'udp_sequential_2',
    'udp_combinatorial_1',
    # unexpected error has occurred (6)
    'xor_top'
]

yosys_unsupported = [
    # System hang-out
    'asym_ram_tdp_write_first',
    # primitive declaration
    'udp_sequential_1',
    'udp_sequential_2',
    'udp_combinatorial_1',
    # $finish, $display
    'finish_ignored_1',
]

print('* Collected Verilog files: %s' % filesqty)
print('* Tool to be used: %s' % tool)

fileno = 1
for filename in files:
    basename = os.path.basename(filename)
    basename = os.path.splitext(basename)[0]
    pathname = os.path.dirname(filename)
    print('* {} ({}/{})'.format(filename, fileno, filesqty))
    fileno += 1
    # Unsupported
    if basename in unsupported:
        print('UNSUPPORTED in ISE and Vivado')
        continue
    if tool=='vivado' and basename in vivado_unsupported:
        print('UNSUPPORTED in Vivado')
        continue
    if 'yosys' in tool and basename in yosys_unsupported:
        print('UNSUPPORTED in Yosys')
        continue
    # Ignore (used later)
    if basename in ['DelayLine', 'FilterStage']:
        print('IGNORED (used as part of another component)')
        continue
    PRJ = Project(tool)
    if 'ise' in tool:
        PRJ.set_part('XC6SLX9-2-CSG324')
    if 'yosys' in tool:
        PRJ.add_files('../../hdl/blackboxes.v')
    PRJ.set_outdir('build/{}/{}'.format(tool, basename))
    if basename in ['EvenSymTranspConvFIR', 'OddSymTranspConvFIR']:
        PRJ.add_files(os.path.join(pathname, '../EvenSymTranspConvFIR_verilog/DelayLine.v'))
        PRJ.add_files(os.path.join(pathname, '../EvenSymTranspConvFIR_verilog/FilterStage.v'))
    PRJ.add_files(filename)
    PRJ.set_top(filename)
    try:
        output = PRJ.generate(to_task='imp', capture=True)
        open('build/{}/{}.txt'.format(tool, basename), 'w').write(output)
    except Exception as e:
        print('FAILED')
        print(('{} ({})'.format(type(e).__name__, e)))
