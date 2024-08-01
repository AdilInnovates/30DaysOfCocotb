import cocotb
from cocotb.triggers import RisingEdge

async def drive_and_check(dut, a, b, expected):
    dut.a <= a
    dut.b <= b
    await RisingEdge(dut.clk)
    assert dut.y == expected, f"Test failed: {dut.a} & {dut.b} != {expected}"

@cocotb.test()
async def and_gate_test(dut):
    await drive_and_check(dut, 0, 0, 0)
    await drive_and_check(dut, 1, 0, 0)
    await drive_and_check(dut, 1, 1, 1)

