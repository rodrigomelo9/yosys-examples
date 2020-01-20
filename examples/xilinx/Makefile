#!/usr/bin/make

ISE=/opt/Xilinx/ise
VIVADO=/opt/Xilinx/vivado

prepare:
	wget -P temp -c www.xilinx.com/txpatches/pub/documentation/misc/xstug_examples.zip
	wget -P temp -c www.xilinx.com/support/documentation/sw_manuals/xilinx2018_3/ug901-vivado-synthesis-examples.zip
	unzip -o -d temp/ise temp/xstug_examples.zip
	unzip -o -d temp/vivado temp/ug901-vivado-synthesis-examples.zip
	# Unsupported things in the Vendor tools
	# * assign_deassign_good.v must be supported in ISE but fails with 14.7.
	rm -fr temp/ise/xstug_examples/Verilog_Language_Support/assign_deassign
	# Invalid/malformed examples
	## Missing generate-for but an index is used.
	rm -fr temp/ise/xstug_examples/HDL_Coding_Techniques/rams/bytewrite_writefirst_test2.v
	## In the header is explained that must be rejected by ISE (could be interestering to check?)
	rm -fr temp/ise/xstug_examples/FPGA_Optimization/primitive_support/primitive_1.v
	# This file seems to be a Zip
	rm -fr temp/vivado/tristates_3.v
	# This file is a VHDL file with stranger things
	rm -fr temp/vivado/procedure_package_1.v

clean-all:
	rm -fr temp build

run-yosys:
	time python3 implement.py -t yosys

run-ise:
	time python3 implement.py -t ise

run-vivado:
	time python3 implement.py -t vivado

run-xilinx: run-ise run-vivado

run-all: run-xilinx run-yosys
