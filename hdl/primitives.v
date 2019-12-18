module primitives (
    input   clk_i,
    input   rst_i,
    input   d1_i,
    input   d2_i,
    input   d3_i,
    output  d1_o,
    output  d2_o,
    output  d3_o
);

    // DFlip-FlopwithSynchronousReset
    FDR inst1 (.C(clk_i), .D(d1_i), .Q(d1_o), .R(rst_i)); 

    // DFlip-FlopwithSynchronousSet
    FDS inst2 (.C(clk_i), .D(d2_i), .Q(d2_o), .S(rst_i)); 

    // DFlip-Flop
    FD  inst3 (.C(clk_i), .D(d3_i), .Q(d3_o));

endmodule
