# Makefile for running Cocotb tests

TOPLEVEL_LANG ?= verilog
SIM ?= icarus
TOPLEVEL := fsm_wrapper
MODULE := test_fsm

export COCOTB_REDUCED_LOG_FMT=1

VERILOG_SOURCES := $(shell pwd)/fsm.v

include $(shell cocotb-config --makefiles)/Makefile.sim
