`timescale 1s / 1s
`include "microplexer.v"

module microplexer_tb();
  
	output wire[3:0] inputs;
  output wire[3:0] sel4;
  input wire wire_in;
	
	// need register to hold values
	reg[3:0] reg_inputs;
  
	initial begin
    $dumpfile("microplexer.vcd");
    $dumpvars(0, microplexer_tb);
	
		reg_inputs = 4'b1000;			// expected wire_in = 0
		#2 reg_inputs = 4'b0100;	// expected wire_in = 0
		#2 reg_inputs = 4'b0010;	// expected wire_in = 0
		#2 reg_inputs = 4'b0001; 	// expected wire_in = 1
    #10 $finish;
  end

	assign inputs = reg_inputs;
	assign sel4 = 4'b0001; // one-hot encoding

	// plug device	
	microplexer MyMicro(wire_in, sel4, inputs);
  
endmodule
