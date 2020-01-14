from glob import glob

from fpga.project import Project

TOOLS = ['ise', 'vivado']

verilogs = glob('temp/**/*.v', recursive=True)

print('* Collected Verilog files: %s' % len(verilogs))

fh = open('build/errors.txt', 'w')
fileno = 1

for verilog in verilogs:
    for tool in TOOLS:
        print('* Processing %d / %d with %s' % (fileno, len(verilogs), tool))
        PRJ = Project(tool)
        PRJ.set_outdir('build/%s' % tool)
        PRJ.add_files(verilog)
        PRJ.set_top(verilog)
        try:
            PRJ.generate(to_task='syn')
        except Exception as e:
            fh.write('* {} - {}'.format(tool, verilog))
            fh.write('{} ({})'.format(type(e).__name__, e))
    fileno += 1
