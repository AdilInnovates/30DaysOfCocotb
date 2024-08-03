# Makefile for running Cocotb tests

TOPLEVEL_LANG ?= verilog
SIM ?= icarus
TOPLEVEL := adder
MODULE := test_adder

export COCOTB_REDUCED_LOG_FMT=1

VERILOG_SOURCES := $(shell pwd)/adder.v

include $(shell cocotb-config --makefiles)/Makefile.sim

