#!/bin/bash
IN=${IN:-"./hello.v"}
OUT=${OUT:-"./hello"}

iverilog -o $OUT $IN
vvp $OUT
