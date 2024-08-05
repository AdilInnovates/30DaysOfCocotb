# Makefile for running Cocotb tests

TOPLEVEL_LANG ?= verilog
SIM ?= icarus
TOPLEVEL := sram_wrapper
MODULE := test_sram

export COCOTB_REDUCED_LOG_FMT=1

VERILOG_SOURCES := $(shell pwd)/sram.v

include $(shell cocotb-config --makefiles)/Makefile.sim
