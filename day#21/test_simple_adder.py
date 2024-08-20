import cocotb
from cocotb.triggers import RisingEdge
import random

@cocotb.test()
async def simple_adder_stress_test(dut):
    for _ in range(1000):  # Stress test with 1000 random inputs
        a = random.randint(0, 15)
        b = random.randint(0, 15)
        expected_sum = a + b

        dut.a.value = a
        dut.b.value = b
        await RisingEdge(dut.clk)

        assert dut.sum.value == expected_sum, f"Adder test failed: {dut.sum.value} != {expected_sum}"

    print("Stress test passed!")

