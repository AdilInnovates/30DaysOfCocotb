// shift_reg.v
module shift_reg #(parameter WIDTH = 8) (
    input wire clk,
    input wire reset,
    input wire shift_in,
    output reg [WIDTH-1:0] data_out
);
    always @(posedge clk or posedge reset) begin
        if (reset)
            data_out <= 0;
        else
            data_out <= {data_out[WIDTH-2:0], shift_in};
    end
endmodule

// shift_reg_wrapper.v
module shift_reg_wrapper #(parameter WIDTH = 8);

    // Signals
    reg clk;
    reg reset;
    reg shift_in;
    wire [WIDTH-1:0] data_out;

    // Instantiate the shift register
    shift_reg #(WIDTH) uut (
        .clk(clk),
        .reset(reset),
        .shift_in(shift_in),
        .data_out(data_out)
    );

    // Initial block for dump setup
    initial begin
        // Set up the dump file and dump variables
        $dumpfile("shift_reg.vcd");
        $dumpvars(0, shift_reg_wrapper);
    end

endmodule

