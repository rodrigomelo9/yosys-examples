#!/usr/bin/make

ISE=/opt/Xilinx/ise
VIVADO=/opt/Xilinx/vivado

prepare:
	wget -P temp -c www.xilinx.com/txpatches/pub/documentation/misc/xstug_examples.zip
	wget -P temp -c www.xilinx.com/support/documentation/sw_manuals/xilinx2018_3/ug901-vivado-synthesis-examples.zip
	unzip -o -d temp/ise temp/xstug_examples.zip
	unzip -o -d temp/vivado temp/ug901-vivado-synthesis-examples.zip
	# This file seems to be a Zip
	rm -fr temp/vivado/tristates_3.v
	# This file is a VHDL file with stranger things
	rm -fr temp/vivado/procedure_package_1.v

clean-all:
	rm -fr temp

run-yosys:
	yosys -Q yosys.tcl

run-ise:
	$(ISE)/ISE/bin/lin64/xtclsh ise.tcl

run-vivado:
	$(VIVADO)/bin/vivado -nolog -nojournal -mode batch -source vivado.tcl
