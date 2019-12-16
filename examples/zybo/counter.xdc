create_clock -name clk_i -period 8 [get_ports clk_i]

set_property PACKAGE_PIN L16 [get_ports clk_i]
set_property IOSTANDARD LVCMOS33 [get_ports clk_i]

set_property PACKAGE_PIN M14     [get_ports leds_o[0]]
set_property IOSTANDARD LVCMOS33 [get_ports leds_o[0]]
set_property PACKAGE_PIN M15     [get_ports leds_o[1]]
set_property IOSTANDARD LVCMOS33 [get_ports leds_o[1]]
set_property PACKAGE_PIN G14     [get_ports leds_o[2]]
set_property IOSTANDARD LVCMOS33 [get_ports leds_o[2]]
set_property PACKAGE_PIN D18     [get_ports leds_o[3]]
set_property IOSTANDARD LVCMOS33 [get_ports leds_o[3]]
