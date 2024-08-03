import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge

@cocotb.test()
async def adder_test(dut):
    clock = cocotb.start_soon(Clock(dut.clk, 10, units='ns').start())

    a = 0b0011  # 3
    b = 0b0101  # 5
    expected_sum = 0b1000  # 8

    dut.a.value = a
    dut.b.value = b

    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)  # Wait for a couple of clock cycles to ensure the sum is computed
    assert dut.sum.value == expected_sum, f"Adder test failed: {dut.sum.value} != {expected_sum}"

    print("Adder test passed!")

