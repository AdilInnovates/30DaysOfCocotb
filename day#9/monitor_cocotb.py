import cocotb
from cocotb.triggers import RisingEdge

class SignalMonitor:
    def __init__(self, signal):
        self.signal = signal
        self.data = []

    async def capture(self):
        while True:
            await RisingEdge(self.signal)
            self.data.append(int(self.signal.value))

@cocotb.test()
async def monitor_test(dut):
    monitor = SignalMonitor(dut.clk)
    cocotb.start_soon(monitor.capture())

    # Drive some signals and check the monitor
    for _ in range(10):
        await RisingEdge(dut.clk)

    print(monitor.data)

