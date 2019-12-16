# Yosys examples

Examples to use Yosys with FPGA boards that I have access to.

## System prepare

* To run ISE examples:
```
export PATH=<ISE_ROOT_PATH>/ISE/bin/lin64:$PATH
```

* To run Vivado examples:
```
export PATH=<VIVADO_ROOT_PATH>/bin:$PATH
```

## How to generate the bitstream

```
make <EXAMPLE_NAME>
```

## How to program

```
make program
```
