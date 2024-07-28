from cocotb.triggers import Timer

@cocotb.test()
async def timer_test(dut):
    await Timer(10, units='ns')
    # Wait for 10 ns

