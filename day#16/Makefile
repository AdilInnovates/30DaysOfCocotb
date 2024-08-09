# Makefile for running Cocotb tests

TOPLEVEL_LANG ?= verilog
SIM ?= icarus
TOPLEVEL := uart_tx_wrapper
MODULE := test_uart_tx

export COCOTB_REDUCED_LOG_FMT=1

VERILOG_SOURCES := $(shell pwd)/uart_tx.v

include $(shell cocotb-config --makefiles)/Makefile.sim

