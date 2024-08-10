// alu.v
module alu (
    input wire clk,
    input wire [3:0] a,
    input wire [3:0] b,
    input wire [1:0] op,
    output reg [3:0] result
);
    always @(posedge clk) begin
        case (op)
            2'b00: result = a + b;
            2'b01: result = a - b;
            2'b10: result = a & b;
            2'b11: result = a | b;
            default: result = 0;
        endcase
    end
endmodule


module alu_wrapper;
    reg [3:0] a;
    reg [3:0] b;
    reg [1:0] op;
    wire [3:0] result;

    alu uut (
      .clk(clk),
      .a(a),
      .b(b),
      .op(op),
      .result(result)
    );

    initial begin
      $dumpfile("alu.vcd");
      $dumpvars(0, alu_wrapper);
    end

endmodule

