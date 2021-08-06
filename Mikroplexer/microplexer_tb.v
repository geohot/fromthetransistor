
module microplexer_tb(
  output reg[5:0] set
);

  initial begin
    set = 6'b000010;
    $display("%b", set);
  end

endmodule
