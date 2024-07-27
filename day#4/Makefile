# Makefile for Cocotb simulation
# SIM ?= icarus
# TOPLEVEL_LANG ?= verilog

TOPLEVEL_LANG = verilog
# Module to be tested
MODULE = test_coroutines
TOPLEVEL = my_module

# Paths to your Verilog source files
VERILOG_SOURCES = $(shell pwd)/my_module.v

# Include Cocotb's makefile
include $(shell cocotb-config --makefiles)/Makefile.sim

