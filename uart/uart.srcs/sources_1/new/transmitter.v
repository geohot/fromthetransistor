`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 09/03/2020 06:28:44 PM
// Design Name: 
// Module Name: transmitter
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
module transmitter(
   input wire      baud_rate_clock,
   input       i_enable,
   input [7:0] i_tx_byte, 
   output reg  o_tx_serial,
   output      o_tx_done,
   output [2:0] o_current_state,
   output [2:0] o_tx_bit_index
 );
 
parameter IDLE = 2'b00;
parameter START = 2'b01;
parameter DATA = 2'b10;
parameter STOP = 2'b11;
   
reg [2:0] current_state = IDLE;
reg [3:0] bit_index = 0;
reg [7:0] r_tx_data = 0;
reg r_tx_done = 0;
     
always @(posedge baud_rate_clock)
begin  
    case (current_state)
        IDLE:
        begin
            r_tx_done <= 1'b0;
            bit_index <= 0;
             
            if (i_enable == 1'b1)
                begin
                    o_tx_serial <= 1'b0;
                    current_state <= START;
                end
            else
                begin
                    o_tx_serial <= 1'b1;
                    current_state <= IDLE;
                end
        end
         
        START:
        begin
            r_tx_data <= i_tx_byte;
            o_tx_serial <= 1'b0;
            current_state <= DATA;
        end
         
        DATA:
        begin
            o_tx_serial <= r_tx_data[bit_index];
            if (bit_index < 8)
                 begin
                      bit_index <= bit_index + 1;
                      current_state <= DATA;
                 end
            else
                begin
                    bit_index <= 0;
                    current_state <= STOP;
                end
        end
         
        STOP:
        begin
            o_tx_serial <= 1'b1;
            r_tx_done <= 1'b1;
        end 
      endcase
    end
 
  assign o_tx_done = r_tx_done;
  assign o_current_state = current_state;
  assign o_tx_bit_index = bit_index;
   
endmodule

