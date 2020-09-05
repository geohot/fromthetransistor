`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 09/03/2020 07:24:28 PM
// Design Name: 
// Module Name: divided_clock
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////
/* clock_divider: used to get the transmitter and receiver to run at the same baud rate.
   This is useful to avoid counting in the transmitter and receiver.
 */
module clock_divider  #(parameter CLK_FREQUENCY = 50000000, parameter BAUD_RATE = 50000000)(
    input i_clock,
    output o_divided_clock  
);

integer clks_per_bit = CLK_FREQUENCY / BAUD_RATE;
integer counter = 1;

reg divided_clock = 0;

always @(posedge i_clock)
    if (counter == clks_per_bit)
        begin
            divided_clock <= ~divided_clock;
            counter <= 0;
        end
   else
        begin
            divided_clock <= divided_clock;
            counter <= counter + 1;
        end
        
   assign o_divided_clock = divided_clock;
endmodule