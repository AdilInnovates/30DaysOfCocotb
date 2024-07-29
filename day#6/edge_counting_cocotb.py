### Edge Counting

@cocotb.test()
async def edge_count_test(dut):
    edge_count = 0
    while edge_count < 10:
        await RisingEdge(dut.clk)
        edge_count += 1
    print(f"Counted {edge_count} rising edges")

