module fsm (
    input wire clk,
    input wire reset,
    input wire in,
    output reg out
);
    reg [1:0] state;
    always @(posedge clk or posedge reset) begin
        if (reset)
            state <= 0;
        else
            case (state)
                0: state <= in ? 1 : 0;
                1: state <= in ? 2 : 0;
                2: state <= in ? 2 : 3;
                3: state <= in ? 1 : 0;
                default: state <= 0;
            endcase
    end
    assign out = (state == 3);
endmodule

// fsm_wrapper.v
module fsm_wrapper (
    input wire clk,
    input wire reset,
    input wire in_value,
    output wire out_value
);

    // Instantiate the FSM module
    fsm fsm_inst (
        .clk(clk),
        .reset(reset),
        .in(in_value),
        .out(out_value)
    );

    // Initial block for dumping waveform
    initial begin
        $dumpfile("fsm.vcd");
        $dumpvars(0, fsm_wrapper);
    end

endmodule


