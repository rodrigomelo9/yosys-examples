# Yosys examples

Examples to use Yosys with FPGA boards that I have access to.

> **Disclaimer:** this project is personal and is not directly related to or
> endorsed by the Yosys project.

## System prepare

* Clone [Yosys](https://github.com/YosysHQ/yosys), compile and install it
(you can also use the provided Dockerfile and scripts).

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

> **NOTE:** you can run `make` to see a list of available examples
> (stored in `hdl/<EXAMPLE>.v`).

## How to program

```
make program
```

## License

Initially based on some examples from [Yosys](https://github.com/YosysHQ/yosys),
which is distributed under an ISC license.

Yosys-examples is distributed under the same [ISC](LICENSE) license.
