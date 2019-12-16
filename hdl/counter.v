module counter(
    input wire clk_i,
    output wire [7:0] leds_o
);

reg [27:0] cnt;

initial cnt = 0;

always @(posedge clk_i)
    cnt <= cnt + 1;

assign leds_o = cnt[27:24];

endmodule
