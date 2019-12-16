#!/usr/bin/make

FPGA=xc7z010clg400-1

OPTS=-nolog -nojournal -mode batch

counter:
	yosys $@.ys
	vivado $(OPTS) -source ../../helpers/vivado.tcl -tclargs $@ $(FPGA)

program:
	vivado $(OPTS) -source ../../helpers/vivado-prog.tcl

clean:
	rm -fr *.html *.xml *.edif *.bit
