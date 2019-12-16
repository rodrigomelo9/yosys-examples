set EXAMPLE [lindex $argv 0]
set PART [lindex $argv 1]

read_xdc $EXAMPLE.xdc
read_edif $EXAMPLE.edif
link_design -part $PART -top $EXAMPLE
opt_design
place_design
route_design
report_utilization
report_timing
write_bitstream -force example_design.bit
