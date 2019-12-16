open_hw_manager
connect_hw_server
open_hw_target
set obj [lindex [get_hw_devices [current_hw_device]] 0]
set_property PROGRAM.FILE example_design.bit $obj
program_hw_devices $obj
