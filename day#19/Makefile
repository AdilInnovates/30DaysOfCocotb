# Makefile for running Cocotb tests

TOPLEVEL_LANG ?= verilog
SIM ?= icarus
TOPLEVEL := interrupt_controller_wrapper
MODULE := test_interrupt_controller

export COCOTB_REDUCED_LOG_FMT=1

VERILOG_SOURCES := $(shell pwd)/interrupt_controller.v

include $(shell cocotb-config --makefiles)/Makefile.sim
