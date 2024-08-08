# Makefile for running Cocotb tests

TOPLEVEL_LANG ?= verilog
SIM ?= icarus
TOPLEVEL := counter_wrapper
MODULE := test_counter

export COCOTB_REDUCED_LOG_FMT=1

VERILOG_SOURCES := $(shell pwd)/counter.v

include $(shell cocotb-config --makefiles)/Makefile.sim
