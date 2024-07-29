### 1.First: Waits for the first trigger to fire. 

from cocotb.triggers import RisingEdge, Timer, First

@cocotb.test()
async def first_trigger_test(dut):
    await First(RisingEdge(dut.clk), Timer(10, units='ns'))
    # Continues as soon as either trigger fires

