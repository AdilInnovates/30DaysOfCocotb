# Makefile for running Cocotb tests

TOPLEVEL_LANG ?= verilog
SIM ?= icarus
TOPLEVEL := alu_wrapper
MODULE := test_alu

export COCOTB_REDUCED_LOG_FMT=1

VERILOG_SOURCES := $(shell pwd)/alu.v

include $(shell cocotb-config --makefiles)/Makefile.sim

