module blinky_testbench();
  
  //  
  output reg clock;
  input wire light_on;

  // initial block is executed once
  initial begin
    // dump file and vars to use in gtkwave
    $dumpfile("test.vcd");
    $dumpvars(0, blinky_testbench);
    // initial value of clock
    clock = 1;
    #100 $finish;
  end
 
  // always block is executed over and over
  // must have a delay (#10) or else it will hang 
  always #1 clock = ~clock;

  // equivalent of putting wires into the blinky module
  blinky U_blinky(clock, light_on);

endmodule
