#!/usr/bin/make

FPGA     = xc7z010clg400-1
EXAMPLES = $(notdir $(basename $(wildcard ../../hdl/*.v)))
OPTS     = -nolog -nojournal -mode batch

all:
	@echo "Available examples: $(EXAMPLES)"

$(EXAMPLES):
	yosys $@.ys
	vivado $(OPTS) -source ../../helpers/vivado.tcl -tclargs $@ $(FPGA)

program:
	vivado $(OPTS) -source ../../helpers/vivado-prog.tcl

clean:
	rm -fr *.html *.xml *.edif *.bit
