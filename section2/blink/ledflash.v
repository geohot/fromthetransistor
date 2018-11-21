// copied from http://community.avnet.com/t5/Spartan-6-LX9-MicroBoard/Looking-for-Blinking-LED-demo-code-explanation/td-p/5454

`timescale 1 ns / 1 ps

module ledflash
  (
  input  wire        CLK_66MHZ,
  input  wire        USER_RESET,
  output wire [3:0]  LED
  );

  //******************************************************************//
  // Create clock.                                                    //
  //******************************************************************//

  wire          clk;
  wire          clknub;
  wire            clk_enable;
  
  assign clk_enable = ~USER_RESET;

  DCM_SP DCM_SP_INST(
    .CLKIN(CLK_66MHZ),
    .CLKFB(clk),
    .RST(1'b0),
    .PSEN(1'b0),
    .PSINCDEC(1'b0),
    .PSCLK(1'b0),
    .DSSEN(1'b0),
    .CLK0(clknub),
    .CLK90(),
    .CLK180(),
    .CLK270(),
    .CLKDV(),
    .CLK2X(),
    .CLK2X180(),
    .CLKFX(),
    .CLKFX180(),
    .STATUS(),
    .LOCKED(),
    .PSDONE());
  defparam DCM_SP_INST.CLKIN_DIVIDE_BY_2 = "FALSE";
  defparam DCM_SP_INST.CLKIN_PERIOD = 15.000;

  BUFGCE  BG (.O(clk), .CE(clk_enable), .I(clknub));

  //*****************************************************************//
  //                                                                  //
  //******************************************************************//

  reg  [26:0] led_count;

  always @(posedge clk) 
      led_count <= led_count + 1;
  
  assign LED[3:0] = led_count[26:23];    // connects led outputs to counter value

endmodule

