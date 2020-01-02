set FILES [
    concat \
        [glob -directory temp/ise/xstug_examples -type f */*.v] \
        [glob -directory temp/ise/xstug_examples -type f */*/*.v] \
        [glob -directory temp/ise/xstug_examples -type f */*/*/*.v] \
        [glob -directory temp/vivado -type f *.v]
]

puts [llength $FILES]

foreach FILE $FILES { puts $FILE }

