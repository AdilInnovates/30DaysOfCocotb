## 2. Combine: Waits for all triggers to fire.

from cocotb.triggers import RisingEdge, Timer, Combine

@cocotb.test()
async def combine_trigger_test(dut):
    await Combine(RisingEdge(dut.clk), Timer(10, units='ns'))
    # Continues after both triggers have fired

