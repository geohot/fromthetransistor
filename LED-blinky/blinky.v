module blinky(
  // ports
  input wire clock, 
  output wire light_on
);
  
  // this is executed every time the clock variable changes
  assign light_on = clock;

endmodule
