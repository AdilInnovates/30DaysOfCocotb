import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer

@cocotb.test()
async def alu_test(dut):
    clock = cocotb.start_soon(Clock(dut.clk, 10, units='ns').start())
    test_vectors = [
        (0b0011, 0b0101, 0b00, 0b1000),  # 3 + 5 = 8
        (0b0110, 0b0010, 0b01, 0b0100),  # 6 - 2 = 4
        (0b1100, 0b1010, 0b10, 0b1000),  # 12 & 10 = 8
        (0b1100, 0b1010, 0b11, 0b1110)   # 12 | 10 = 14
    ]

    await FallingEdge(dut.clk)
    for a, b, op, expected in test_vectors:
        dut.a.value = a
        dut.b.value = b
        dut.op.value = op
        await FallingEdge(dut.clk)
        assert dut.result.value == expected, f"ALU test failed: {dut.result.value} != {expected}"

    print("ALU test passed!")

