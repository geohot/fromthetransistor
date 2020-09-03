`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 09/01/2020 08:55:37 PM
// Design Name: 
// Module Name: receiver
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
    input baud_rate_clock,
    input serial_connection,
    output reg [7:0] data
);
parameter IDLE = 2'b00;
parameter START = 2'b01;
parameter DATA = 2'b10;
parameter END = 2'b11;

reg transmission_state = IDLE;

integer byte_index = 0;

reg stable_serial_data = 1'b1;

always @(posedge baud_rate_clock)
begin
    case (transmission_state)
        IDLE:
        begin
            if (serial_connection <= 1'b0)
                transmission_state <= START;
            else
                transmission_state <= IDLE;
        end
        START:
        begin
            transmission_state <= DATA;
        end
        
        DATA:
        begin
            if (byte_index < 8)
            begin
                data[byte_index] <= serial_connection;
                byte_index <= byte_index + 1;
            end
            else
            begin
                transmission_state <= END;
                byte_index <= 0;
            end
        end
        
        END:
        begin
            transmission_state <= IDLE;
        end
        
        default:
        begin
        end
    endcase
end

// baud_rate_clock = clocks_per_second / bits_per_second
endmodule
