// sram.v
module sram (
    input wire clk,
    input wire we,
    input wire [3:0] addr,
    input wire [7:0] data_in,
    output reg [7:0] data_out
);
    reg [7:0] mem [0:15];

    always @(posedge clk) begin
        if (we)
            mem[addr] <= data_in;
        data_out <= mem[addr];
    end
endmodule

module sram_wrapper;

    reg clk;
    reg we;
    reg [3:0] addr;
    reg [7:0] data_in;
    wire [7:0] data_out;

    // Instantiate the SRAM module
    sram uut (
        .clk(clk),
        .we(we),
        .addr(addr),
        .data_in(data_in),
        .data_out(data_out)
    );

    initial begin
        // Dump file setup
        $dumpfile("sram.vcd");
        $dumpvars(0, sram_wrapper);
    end

endmodule
