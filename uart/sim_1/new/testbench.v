`timescale 1ns / 1ps
`include "transmitter.v"
`include "receiver.v"
`include "clock_divider.v"

//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 09/02/2020 06:16:42 PM
// Design Name: 
// Module Name: testbench
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


module testbench;

// Transmitter clock
reg transmitter_clock = 0;
wire transmitter_divided_clock;

clock_divider UUT_Transmitter(
    .clock(transmitter_clock),
    .clocks_per_second(100000000),
    .desired_clocks_per_second(1), // 1 clocks per second
    .divided_clock(transmitter_divided_clock)
);

always #5 transmitter_clock = ~transmitter_clock; // every 5 ns, flip signal, 10ns clock cycle = 100Mhz

// Receiver clock
reg receiver_clock = 0;
wire receiver_divided_clock;

clock_divider UUT_Receiver (
    .clock(receiver_clock),
    .clocks_per_second(100000000),
    .desired_clocks_per_second(1), // 1 clocks per second
    .divided_clock(receiver_divided_clock)
);

always #5 receiver_clock = ~receiver_clock; // every 5 ns, flip signal, 10ns clock cycle = 100Mhz

// Transmitter

/*
reg [7:0] transmitter_data = 0;
reg transmitter_enable = 0;

wire transmitter_serial_connection;
wire transmitter_done;

transmitter Transmitter(
    .baud_rate_clock(transmitter_divided_clock),
    .data(transmitter_data),
    .enable(transmitter_enable),
    .serial_connection(transmitter_serial_connection),
    .done(transmitter_done)
);
   
 */
   /* 
reg [7:0] reciever_data = 0;

// Receiver
reciever Receiver(
    .baud_rate_clock(reciever_divided_clock),
    .serial_connection(transmitter_serial_connection),
    .data(reciever_data)
);

initial
    begin
        @(posedge transmitter_clock);
        transmitter_enable <= 1'b1;
        transmitter_data <= 8'hAB;
        @(posedge transmitter_done);
        
        if (reciever_data == 8'hAB)
            $display("Test Passed - Correct Byte Recieved!");
        else
            $display("Test Failed - Incorrect Byte Recieved :(");
    end
*/
endmodule

