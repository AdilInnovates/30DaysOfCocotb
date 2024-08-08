import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge

@cocotb.test()
async def counter_test(dut):
    clock = cocotb.start_soon(Clock(dut.clk, 10, units='ns').start())

    dut.reset.value = 1
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)
    assert dut.count.value == 0, f"Counter reset test failed: {dut.count.value} != 0"

    dut.reset.value = 0
    dummy_counter=0

    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)
    for _ in range(20):
        dummy_counter=dummy_counter+1
        if dummy_counter == 16:
            dummy_counter = 0
        assert dut.count.value == dummy_counter, f"Counter test failed: {dut.count.value} != {dummy_counter}"
        cocotb.log.info(f"Counter test failed: {dut.count.value} != {dummy_counter}")
        await RisingEdge(dut.clk)
        # await RisingEdge(dut.clk)

    print("Counter test passed!")

