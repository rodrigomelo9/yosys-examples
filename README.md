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
make <EXAMPLE>
```

> **NOTE:** valid examples in `hdl/<EXAMPLE>.v`.

## How to program

```
make program
```

## License

Initially based on some examples from [Yosys](https://github.com/YosysHQ/yosys), which are distributed under an ISC license.

Yosys-examples is distributed under the same [ISC](LICENSE) license.
