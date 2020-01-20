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
	# Duplicated
	# find -name *.v -type f -printf '%p %f\n' | sort -t ' ' -k 2,2 | uniq -f 1 --all-repeated=separate | cut -d' ' -f1
	rm -fr temp/ise/xstug_examples/HDL_Coding_Techniques/dsp/OddSymTranspConvFIR_verilog/DelayLine.v
	rm -fr temp/ise/xstug_examples/HDL_Coding_Techniques/dsp/OddSymTranspConvFIR_verilog/FilterStage.v
	rm -fr temp/vivado/bytewrite_ram_1b.v
	rm -fr temp/vivado/dynamic_shift_registers_1.v
	rm -fr temp/vivado/functions_constant.v
	rm -fr temp/vivado/finish_ignored_1.v
	rm -fr temp/vivado/finish_supported_1.v
	rm -fr temp/vivado/functions_1.v
	rm -fr temp/vivado/parameter_1.v
	rm -fr temp/vivado/parameter_generate_for_1.v
	rm -fr temp/vivado/shift_registers_0.v
	rm -fr temp/vivado/shift_registers_1.v
	rm -fr temp/vivado/tasks_1.v
	rm -fr temp/vivado/tristates_1.v
	rm -fr temp/vivado/tristates_2.v

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
