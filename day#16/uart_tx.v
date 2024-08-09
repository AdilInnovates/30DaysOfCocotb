// uart_tx.v
module uart_tx (
    input wire clk,
    input wire reset,
    input wire [7:0] data_in,
    input wire start,
    output reg tx,
    output reg busy
);
    reg [3:0] bit_cnt;
    reg [7:0] uart_tx;
    reg [7:0] uart_frame;
    reg uart_start;
    
    always @(posedge clk or posedge reset) begin
        if (reset) begin
            tx <= 1'b1;
            busy <= 1'b0;
            uart_start <= 1'b0;
            bit_cnt <= 4'd0;
            uart_tx <= 8'd0;
        end else begin
            if (start && !busy) begin
                busy <= 1'b1;
                tx <= 1'b0;
                uart_frame <= {data_in};
                bit_cnt <= 4'd10;
            end

            else if (bit_cnt > 0) begin
                {tx, uart_frame} <= {uart_frame, 1'b1};
                bit_cnt <= bit_cnt - 1'b1;
                if (bit_cnt == 1)
                    busy <= 1'b0;
            end else begin
                tx <= 1'b1;
            end
        end
    end
endmodule

// UART wrapper
module uart_tx_wrapper;

  reg clk;
  reg reset;
  reg [7:0] data_in;
  reg start;
  wire tx;
  wire busy;

  uart_tx uut (
    .clk(clk),
    .reset(reset),
    .data_in(data_in),
    .start(start),
    .tx(tx),
    .busy(busy)
  );

  initial begin
    $dumpfile("uart_tx.vcd");
    $dumpvars(0, uart_tx_wrapper);
  end

endmodule
