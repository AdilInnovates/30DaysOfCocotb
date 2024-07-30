import cocotb
from cocotb.triggers import RisingEdge

@cocotb.test()
async def vpi_example_test(dut):
    await RisingEdge(dut.clk)
    print(f"Signal value: {dut.signal_name.value}")



