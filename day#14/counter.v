// counter.v
module counter (
    input wire clk,
    input wire reset,
    output reg [3:0] count
);
    always @(posedge clk or posedge reset) begin
        if (reset)
            count <= 4'b0000;
        else
            count <= count + 1;
    end
endmodule

// counter_wrapper.v
module counter_wrapper (
    input wire clk,
    input wire reset,
    output reg [3:0] count
);

    // Instantiate the counter module
    counter counter_inst (
        .clk(clk),
        .reset(reset),
        .count(count)
    );

    // Initial block for dumping waveform
    initial begin
        $dumpfile("counter.vcd");
        $dumpvars(0, counter_wrapper);
    end

endmodule

