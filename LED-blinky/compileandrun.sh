#!/bin/bash

echo "compiling";
iverilog -o blinky.vvp blinky_tb.v
echo "runing"; 
vvp blinky.vvp
