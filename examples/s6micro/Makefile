#!/usr/bin/make

FPGA     = xc6slx9csg324-2
EXAMPLES = $(notdir $(basename $(wildcard ../../hdl/*.v)))

all:
	@echo "Available examples: $(EXAMPLES)"

$(EXAMPLES):
	yosys $@.ys
	edif2ngd $@.edif
	ngdbuild $@ -uc $@.ucf -p $(FPGA)
	map -w $@
	par -w $@.ncd example_design.ncd
	bitgen -w example_design.ncd -g StartupClk:JTAGClk

program:
	impact -batch ../../helpers/program.impact

clean:
	rm -fr _xmsgs xlnx_auto_0_xdb
	rm -fr *.html *.xml *.xrpt *.log *.csv *.txt *.lst
	rm -fr *.bld *.edif *.map *.mrp *.ncd *.ngd *.ngm *.ngo *.pcf
	rm -fr *.bgn *.bit *.drc *.pad *.par *.ptwx *.unroutes *.xpi *.xwbt

