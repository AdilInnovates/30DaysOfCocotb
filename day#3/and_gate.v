// and_gate.v
module and_gate(
    input wire clk,
    input wire a,
    input wire b,
    output reg y
);
    always @(posedge clk) begin
        y <= a & b;
    end
endmodule
