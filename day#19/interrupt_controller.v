// interrupt_controller.v
module interrupt_controller (
    input wire clk,
    input wire reset,
    input wire [3:0] irq,
    output reg irq_ack
);
    always @(posedge clk or posedge reset) begin
        if (reset)
            irq_ack <= 0;
        else
            irq_ack <= |irq;
    end
endmodule

module interrupt_controller_wrapper;
    reg clk;
    reg reset;
    reg [3:0] irq;
    wire irq_ack;

    interrupt_controller uut (
        .clk(clk),
        .reset(reset),
        .irq(irq),
        .irq_ack(irq_ack)
    );

    initial begin
        $dumpfile("interrupt_controller.vcd");
        $dumpvars(0, interrupt_controller_wrapper);
    end

endmodule
