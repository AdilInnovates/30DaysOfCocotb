import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge

@cocotb.test()
async def shift_reg_test(dut):
    clock = cocotb.start_soon(Clock(dut.clk, 10, units='ns').start())

    dut.reset.value = 1
    await RisingEdge(dut.clk)
    dut.reset.value = 0

    dut.shift_in.value = 1
    width = int(dut.WIDTH)
    await RisingEdge(dut.clk)
    for shift in range(width):
        cocotb.log.info(f"Shift Register Output : {dut.data_out.value}")
        assert dut.data_out.value == ((1 << (shift)) - 1), f"Shift register test failed: {dut.data_out.value} != {(1 << (shift)) - 1}"
        await RisingEdge(dut.clk)

    assert dut.data_out.value == ((1 << (width)) - 1), f"Shift register test failed: {dut.data_out.value} != {(1 << (width)) - 1}"

    print("Shift register test passed!")

