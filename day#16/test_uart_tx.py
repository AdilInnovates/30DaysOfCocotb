import cocotb
import random
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer

@cocotb.test()
async def uart_tx_test(dut):
    clock = cocotb.start_soon(Clock(dut.clk, 10, units='ns').start())

    regression = random.randint(0,255)
    # Reset DUT
    dut.reset.value = 1
    await FallingEdge(dut.clk)
    await FallingEdge(dut.clk)
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    # Test data transmission
    dut.data_in.value = 0x55  # 0x55 = 01010101
    dut.start.value = 1
    await FallingEdge(dut.clk)
    dut.start.value = 0

    # Expected UART frame for 0x55: start bit (0) + data bits + stop bit (1)
    expected_frame = [0, 0, 1, 0, 1, 0, 1, 0, 1, 1]

    for bit in expected_frame:
        assert dut.tx.value == bit, f"UART TX test failed: expected {bit}, got {dut.tx.value}"
        await FallingEdge(dut.clk)

    for test_no in range(regression):
        expected_frame = []
        data_input = random.randint(0,255)
        # Test data transmission
        dut.data_in.value = data_input
        dut.start.value = 1
        await FallingEdge(dut.clk)
        dut.start.value = 0

        # Start bit (0)
        expected_frame.append(0)
        
        # Append each bit of data_input from MSB to LSB
        for i in range(7, -1, -1):  # Iterate from 7 to 0
            expected_frame.append((data_input >> i) & 1)

        # Stop bit (1)
        expected_frame.append(1)


        for bit in expected_frame:
            assert dut.tx.value == bit, f"UART TX test failed: expected {bit}, got {dut.tx.value}"
            await FallingEdge(dut.clk)



    print("UART TX test passed!")

