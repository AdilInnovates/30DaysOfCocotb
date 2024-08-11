// dual_clock_fifo.v
module dual_clock_fifo (
    input wire wr_clk,
    input wire rd_clk,
    input wire reset,
    input wire [7:0] data_in,
    input wire wr_en,
    input wire rd_en,
    output reg [7:0] data_out,
    output reg full,
    output reg empty
);
    reg [7:0] fifo [15:0];
    reg [3:0] wr_ptr, rd_ptr;
    reg [4:0] fifo_cnt;

    always @(posedge wr_clk or posedge reset) begin
        if (reset) begin
            wr_ptr <= 0;
            fifo_cnt <= 0;
            full <= 0;
        end else if (wr_en && !full) begin
            fifo[wr_ptr] <= data_in;
            wr_ptr <= wr_ptr + 1;
            fifo_cnt <= fifo_cnt + 1;
            if (fifo_cnt == 15) full <= 1;
            empty <= 0;
        end
    end

    always @(posedge rd_clk or posedge reset) begin
        if (reset) begin
            rd_ptr <= 0;
            empty <= 1;
        end else if (rd_en && !empty) begin
            data_out <= fifo[rd_ptr];
            rd_ptr <= rd_ptr + 1;
            fifo_cnt <= fifo_cnt - 1;
            if (fifo_cnt == 0) empty <= 1;
            full <= 0;
        end
    end
endmodule

module dual_clock_fifo_wrapper;
    reg wr_clk;
    reg rd_clk;
    reg reset;
    reg [7:0] data_in;
    reg wr_en;
    reg rd_en;
    wire [7:0] data_out;
    wire full;
    wire empty;

    dual_clock_fifo uut (
      .wr_clk(wr_clk),
      .rd_clk(rd_clk),
      .reset(reset),
      .data_in(data_in),
      .wr_en(wr_en),
      .rd_en(rd_en),
      .data_out(data_out),
      .full(full),
      .empty(empty)
    );

    initial  begin
      $dumpfile("dual_clock_fifo.vcd");
      $dumpvars(0, dual_clock_fifo_wrapper);
    end



endmodule
