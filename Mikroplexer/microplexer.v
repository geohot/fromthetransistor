// this is a simple implementation of a microplexer.
// the difference between a microplexer and a LUT is that 
// a lut has programmable memory for the inputs
// that way they can manually decide where the current goes
// so that they can implement advanced hardware digitally

module microplexer(
  output wire wire_out,
  input wire[3:0] sel4,
  input wire[3:0] inputs
);
  
  assign wire_out = (inputs[3] & sel4[3]) || 
                    (inputs[2] & sel4[2]) || 
                    (inputs[1] & sel4[1]) || 
                    (inputs[0] & sel4[0]);

endmodule
