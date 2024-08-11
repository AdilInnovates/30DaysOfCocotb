import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer

@cocotb.test()
async def dual_clock_fifo_test(dut):
    wr_clock = cocotb.start_soon(Clock(dut.wr_clk, 10, units='ns').start())
    rd_clock = cocotb.start_soon(Clock(dut.rd_clk, 15, units='ns').start())

    dut.reset.value = 1
    await FallingEdge(dut.wr_clk)
    await FallingEdge(dut.rd_clk)
    dut.reset.value = 0

    # Write data to FIFO
    dut.data_in.value = 0xA5
    dut.wr_en.value = 1
    await FallingEdge(dut.wr_clk)
    dut.wr_en.value = 0

    # Wait a few clock cycles for synchronization
    for _ in range(3):
        await FallingEdge(dut.rd_clk)

    # Read data from FIFO
    dut.rd_en.value = 1
    await FallingEdge(dut.rd_clk)
    dut.rd_en.value = 0

    assert dut.data_out.value == 0xA5, f"Dual-clock FIFO test failed: {dut.data_out.value} != 0xA5"

    print("Dual-clock FIFO test passed!")

