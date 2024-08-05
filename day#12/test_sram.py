import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge

@cocotb.test()
async def sram_test(dut):
    clock = cocotb.start_soon(Clock(dut.clk, 10, units='ns').start())

    ### Giving the initial values 
    dut.we.value = 1
    dut.addr.value = 0xA
    dut.data_in.value = 0x55

    await RisingEdge(dut.clk)
    ### Waiting for the signals to get transfered onto the line 
    await RisingEdge(dut.clk)
    dut.we.value = 0
    print(f"Value of output: {dut.data_out.value}")
    await RisingEdge(dut.clk)
    print(f"Value of output: {dut.data_out.value}")
    assert dut.data_out.value == 0x55, f"SRAM test failed: {dut.data_out.value} != 0x55"

    print("SRAM test passed!")

