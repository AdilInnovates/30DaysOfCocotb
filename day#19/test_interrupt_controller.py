import cocotb
import random
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def interrupt_controller_test(dut):
    clock = cocotb.start_soon(Clock(dut.clk, 10, units='ns').start())

    tests_to_run=random.randint(0,255)
    dut.reset.value = 1
    await FallingEdge(dut.clk)
    dut.reset.value = 0

    dut.irq.value = 0b0001
    await FallingEdge(dut.clk)
    assert dut.irq_ack.value == 1, f"Interrupt controller test failed: {dut.irq_ack.value} != 1"

    dut.irq.value = 0b0000
    await FallingEdge(dut.clk)
    assert dut.irq_ack.value == 0, f"Interrupt controller test failed: {dut.irq_ack.value} != 0"

    for test_no in range(tests_to_run):
        input_value=random.randint(0,15)
        dut.irq.value = input_value
        await FallingEdge(dut.clk)
        assert dut.irq_ack.value == (input_value != 0), f"Interrupt controller test failed: {dut.irq_ack.value} != {input_value != 0}"

    print("Interrupt controller test passed!")

