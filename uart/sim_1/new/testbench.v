`timescale 1ns / 1ps


/////////////////////////////////////////////////////////////////////////////////
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
    .divided_clock(transmitter_divided_clock)
);


// Receiver clock
reg receiver_clock = 0;
wire receiver_divided_clock;

clock_divider UUT_Receiver (
    .clock(receiver_clock),
    .divided_clock(receiver_divided_clock)
);

always #5
begin
    transmitter_clock = ~transmitter_clock; // every 5 ns, flip signal, 10ns clock cycle = 100Mhz
    receiver_clock = ~receiver_clock; // every 5 ns, flip signal, 10ns clock cycle = 100Mhz
end

// Transmitter
reg [7:0] transmitter_data = 0;
reg transmitter_enable = 0;

wire transmitter_serial_connection = 1;
wire transmitter_done;
wire [2:0] transmission_state;
wire [2:0] byte_index = 0;

transmitter Transmitter(
    .baud_rate_clock(transmitter_divided_clock),
    .data(transmitter_data),
    .enable(transmitter_enable),
    .o_transmission_state(transmission_state),
    .serial_connection(transmitter_serial_connection),
    .done(transmitter_done),
    .o_byte_index(byte_index)
);
   

// Receiver
wire [7:0] reciever_data;

receiver Receiver(
    .baud_rate_clock(reciever_divided_clock),
    .serial_connection(transmitter_serial_connection),
    .data(reciever_data)
);

initial
    begin
        @(posedge transmitter_clock);
        transmitter_data <= 8'hAB;
        transmitter_enable <= 1'b1;
        @(posedge transmitter_done);
        
        if (reciever_data == 8'hAB)
            $display("Test Passed - Correct Byte Recieved!");
        else
            $display("Test Failed - Incorrect Byte Recieved :(");
    end
endmodule

