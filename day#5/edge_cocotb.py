from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def edge_trigger_test(dut):
    await RisingEdge(dut.clk)
    # Do something on rising edge
    await FallingEdge(dut.clk)
    # Do something on falling edge

