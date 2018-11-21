#!/bin/bash

# synthesize the verilog
#xilinx xst -ifn go.scr

# ngdbuild? turns netlist into Native Generic Database?
#xilinx ngdbuild -p spartan6 go.ngc go.ngd

# map
xilinx map -p xc6slx9-csg324 -w go.ngd -o go.map.ncd go.pcf

