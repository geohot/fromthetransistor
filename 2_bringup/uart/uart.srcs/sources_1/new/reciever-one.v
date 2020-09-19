`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 09/03/2020 06:31:27 PM
// Design Name: 
// Module Name: reciever
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

module receiver(
   input        i_Clock,
   input        serial_connection,
   output reg [7:0] r_Rx_Byte = 0
   );
    
  parameter IDLE = 2'b00;
  parameter START = 2'b01;
  parameter DATA = 2'b10;
  parameter STOP = 2'b11;
     
  reg r_Rx_Data_R = 1'b1;
  reg r_Rx_Data   = 1'b1;
   
  reg [3:0] bit_index = 0;
//  reg [7:0] r_Rx_Byte = 0;
  reg [2:0] current_state = IDLE;
    
  always @(posedge i_Clock)
    begin
      case (current_state)
        IDLE:
          begin
            if (serial_connection == 1'b0)
            begin
                current_state <= START;
            end
            else
            begin
                current_state <= IDLE;
            end
          end
         
        START:
          begin
            current_state <= DATA;
          end
         
        DATA:
          begin
            if (bit_index < 8)
                begin
                    r_Rx_Byte[bit_index] = serial_connection;
                    bit_index = bit_index + 1;
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
            current_state <= IDLE;
          end
         
      endcase
    end   
   
  assign o_Rx_Byte = r_Rx_Byte;
   
endmodule
