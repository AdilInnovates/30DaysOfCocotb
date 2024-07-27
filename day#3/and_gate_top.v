

// testbench.v
module and_gate_top(
    input wire clk,
    input wire a,
    input wire b,
    output reg y
);


    // Instantiate the and_gate module
    and_gate uut (
        .clk(clk),
        .a(a),
        .b(b),
        .y(y)
    );

    initial begin
        // Dump waveform data
        $dumpfile ("and_gate.vcd");
        $dumpvars (0, and_gate_top);
    end

endmodule

