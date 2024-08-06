import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge

@cocotb.test()
async def test_fsm(dut):
    """Test FSM module."""
    clock = cocotb.start_soon(Clock(dut.clk, 10, units='ns').start())

    # Reset the DUT
    dut.reset.value = 1
    dut.in_value.value = 0
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)
    dut.reset.value = 0

    # Apply input and check output
    for i in range(4):
        dut.in_value.value = i % 2  # Toggle the input
        await RisingEdge(dut.clk)
        cocotb.log.info(f'Input: {dut.in_value.value} | Output: {dut.out_value.value}')


