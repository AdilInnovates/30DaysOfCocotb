import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def simple_module_test(dut):
    clock = cocotb.start_soon(Clock(dut.clk, 10, units='ns').start())

    dut.reset.value = 1
    await FallingEdge(dut.clk)
    dut.reset.value = 0

    dut.in_value.value = 0xA
    await FallingEdge(dut.clk)
    assert dut.out_value.value == 0xA, f"Simple module test failed: {dut.out_value.value} != 0xA"

    # Functional Coverage (example using manual counters)
    coverage = set()
    for i in range(16):
        dut.in_value.value = i
        await FallingEdge(dut.clk)
        coverage.add(dut.out_value.value.integer)

    assert len(coverage) == 16, f"Functional coverage incomplete: {coverage}"

    print("Advanced assertions and coverage test passed!")

