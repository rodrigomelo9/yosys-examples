#!/usr/bin/make

EXAMPLES=$(wildcard examples/*)

.PHONY: clean


docker-build:
	docker build -t yosys-pyfpga -f Dockerfile .

docker-run:
	bash docker-run.sh

clean:
	@$(foreach EXAMPLE,$(EXAMPLES), make -C $(EXAMPLE) clean;)
