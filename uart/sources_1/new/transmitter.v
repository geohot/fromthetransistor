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
    input baud_rate_clock,
    input [7:0] data,
    input enable,
    output [2:0] o_transmission_state,
    output reg serial_connection,
    output done,
    output [2:0] o_byte_index
);
parameter IDLE = 2'b00;
parameter START = 2'b01;
parameter DATA = 2'b10;
parameter END = 2'b11;

reg [2:0] transmission_state = IDLE;
reg [2:0] byte_index = 0;

reg r_done = 1'b0;

always @(posedge baud_rate_clock)
begin
    case (transmission_state)
        IDLE:
        begin
            if (enable == 1'b1)
            begin
                transmission_state <= START;
                serial_connection <= 1'b0;
            end
            else
            begin
                transmission_state <= IDLE;
                serial_connection <= 1'b1;
                r_done <= 1'b1;
            end
        end
        START:
        begin
            serial_connection <= 1'b0;
            transmission_state <= DATA;
        end
        
        DATA:
        begin
            if (byte_index < 7)
            begin
                serial_connection <= data[byte_index];
                byte_index <= byte_index + 1;
                transmission_state <= DATA;
            end
            else
            begin
                byte_index <= 0;
                serial_connection <= 1'b1;
                transmission_state <= END;
            end
        end
        
        END:
        begin
            serial_connection <= 1'b1;
            transmission_state <= IDLE;
            r_done <= 1'b1;
        end
        
        default:
        begin
        end
    endcase
end

assign done = r_done;
assign o_transmission_state = transmission_state;
assign o_byte_index = byte_index;
// baud_rate_clock = clocks_per_second / bits_per_second
endmodule

