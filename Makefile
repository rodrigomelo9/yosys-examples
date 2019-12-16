#!/usr/bin/make

EXAMPLES=$(wildcard examples/*)

.PHONY: clean

clean:
	@$(foreach EXAMPLE,$(EXAMPLES), make -C $(EXAMPLE) clean;)
