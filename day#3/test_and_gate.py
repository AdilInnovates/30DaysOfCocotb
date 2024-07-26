import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge

@cocotb.test()
async def and_gate_test(dut):
    # Generate the clock
    clock = cocotb.start_soon(Clock(dut.clk, 10, units='ns').start(start_high=False))

    # Initialize inputs
    dut.a.value = 0
    dut.b.value = 0

    # Wait for a clock edge
    await RisingEdge(dut.clk)

    # Apply test vectors
    dut.a.value = 1
    await RisingEdge(dut.clk)  # Wait for the clock edge to apply the input
    print(f"dut.y.value: {dut.y.value}")
    assert dut.y.value == 0, "Test failed with a=1, b=0"

    dut.b.value = 1
    await RisingEdge(dut.clk)  # Wait for the clock edge to apply the input

    # Print the current values of 'a' and 'b'
    print(f"dut.a.value: {dut.a.value}")
    print(f"dut.b.value: {dut.b.value}")

    await RisingEdge(dut.clk)  # Wait for the next clock edge for the output to update
    print(f"dut.y.value: {dut.y.value}")
    assert dut.y.value == 1, "Test failed with a=1, b=1"

    print("All tests passed!")

