`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 08/29/2020 03:38:54 PM
// Design Name: 
// Module Name: clock_divider
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


module clock_divider(
input wire clock, // 100MHz = 100M clock cycles/sec
output reg divided_clock = 0// 1Hz => 0.5s on, 0.5s off
    );
integer counter = 1;

localparam div_value = 50000000; // if we want div_clock to run once a second, div_value = clock cycles. ex. 1Hz = 1000

// runs every clock cycle
always @(posedge clock) // sensitivity list
begin
    if (counter == div_value)
        begin
            divided_clock = ~divided_clock; // flip signal
            counter <= 0;
        end
   else
        begin
            // = sequential assignment
            // <= parallel assignment
            divided_clock <= divided_clock;
            counter <= counter + 1;
        end
   end
        
endmodule
