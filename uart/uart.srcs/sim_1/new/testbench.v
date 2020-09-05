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

// transmitter clock
  reg transmitter_clock = 0;
  wire transmitter_divided_clock;
  
  clock_divider
  #(.CLK_FREQUENCY(25000000), .BAUD_RATE(25000000))
  Transmitter_Clock_Divider(
    .i_clock(transmitter_clock),
    .o_divided_clock(transmitter_divided_clock)
  );
   
  always #5
    begin
      transmitter_clock = ~transmitter_clock;
    end
    
// receiver clock
  reg receiver_clock = 0;
  wire receiver_buad_rate_clock;
  
  clock_divider
  #(.CLK_FREQUENCY(25000000), .BAUD_RATE(25000000))
  Receiver_Clock_Divider(
    .i_clock(receiver_clock),
    .o_divided_clock(receiver_baud_rate_clock)
  );
   
  always #5
    begin
      receiver_clock = ~receiver_clock;
    end
    
// transmitter
  reg transmitter_enable = 1;
  reg [7:0] transmitter_data = 0;
  
  wire [2:0] o_tx_current_state;
  wire transmitter_done;
  wire o_tx_serial;
  wire [2:0] o_tx_bit_index;

  transmitter Transmitter(
    .baud_rate_clock(transmitter_divided_clock),
    .i_enable(transmitter_enable),
    .i_tx_byte(transmitter_data),
    .o_tx_serial(o_tx_serial),
    .o_tx_done(transmitter_done),
    .o_current_state(o_tx_current_state),
    .o_tx_bit_index(o_tx_bit_index)
  );
    
 // receiver
 wire [7:0] o_Rx_Byte;
 
 receiver Receiver(
   .i_Clock(receiver_baud_rate_clock),
   .serial_connection(o_tx_serial),
   .r_Rx_Byte(o_Rx_Byte)
   );

 // Test
  initial
    begin
      @(posedge transmitter_clock);
      transmitter_enable <= 1;
      transmitter_data <= 8'hAB;
      @(posedge transmitter_done);
      $display("Transmitter is done sending data!");
      
      if (o_Rx_Byte == 8'hAB)
      begin
        $display("Tests Passed - Correct Byte Received!!");
      end
      else
      begin
        $display("Tests Failed - Incorrect Byte Received :(");
      end
    end
   
endmodule

