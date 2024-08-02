import cocotb
from cocotb.triggers import RisingEdge

class Scoreboard:
    def __init__(self):
        self.expected = []
        self.actual = []

    def add_expected(self, value):
        self.expected.append(value)

    def add_actual(self, value):
        self.actual.append(value)

    def compare(self):
        assert self.expected == self.actual, f"Mismatch: {self.expected} != {self.actual}"

@cocotb.test()
async def scoreboard_test(dut):
    scoreboard = Scoreboard()

    for i in range(10):
        dut.input <= i
        await RisingEdge(dut.clk)
        scoreboard.add_expected(i)
        scoreboard.add_actual(int(dut.output.value))

    scoreboard.compare()

