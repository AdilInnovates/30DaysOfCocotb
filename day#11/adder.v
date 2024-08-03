// adder.v
module adder (
    input wire clk,
    input wire [3:0] a,
    input wire [3:0] b,
    output reg [4:0] sum
);

    always @(posedge clk) begin
        sum <= a + b;
    end

endmodule


