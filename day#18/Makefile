# Makefile for running Cocotb tests

TOPLEVEL_LANG ?= verilog
SIM ?= icarus
TOPLEVEL := dual_clock_fifo_wrapper
MODULE := test_dual_clock_fifo

export COCOTB_REDUCED_LOG_FMT=1

VERILOG_SOURCES := $(shell pwd)/dual_clock_fifo.v

include $(shell cocotb-config --makefiles)/Makefile.sim
