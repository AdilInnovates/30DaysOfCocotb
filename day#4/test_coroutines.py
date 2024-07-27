import cocotb
from cocotb.triggers import Timer

@cocotb.coroutine
async def test_coroutine(dut, check):
    dut.in_sig.value = 1
    await Timer(10, units='ns')
    print(f"check: async-{check}")
    await Timer(10, units='ns')
    print(f"check: async-{check}")
    assert dut.out_sig.value == 1, "Test failed!"

@cocotb.test()
async def run_test(dut):
    await test_coroutine(dut, 1)
    await test_coroutine(dut, 2)

