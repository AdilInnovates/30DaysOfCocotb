// simple_module.v
module simple_module (
    input wire clk,
    input wire reset,
    input wire [3:0] in_value,
    output reg [3:0] out_value
);
    always @(posedge clk or posedge reset) begin
        if (reset)
            out_value <= 0;
        else
            out_value <= in_value;
    end
endmodule

module simple_module_wrapper;
    reg clk;
    reg reset;
    reg [3:0] in_value;
    wire [3:0] out_value;

    simple_module uut(
        .clk(clk),
        .reset(reset),
        .in_value(in_value),
        .out_value(out_value)
    );

    initial begin
      $dumpfile("simple_module.vcd");
      $dumpvars(0, simple_module_wrapper);
    end

endmodule 

