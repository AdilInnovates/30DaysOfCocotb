# Makefile for running Cocotb tests

TOPLEVEL_LANG ?= verilog
SIM ?= icarus
TOPLEVEL := simple_module_wrapper
MODULE := test_simple_module

export COCOTB_REDUCED_LOG_FMT=1

VERILOG_SOURCES := $(shell pwd)/simple_module.v

include $(shell cocotb-config --makefiles)/Makefile.sim
