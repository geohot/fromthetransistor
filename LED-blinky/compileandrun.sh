#!/bin/bash

iverilog -o blinky_tp.vvp blinky_tb.v
vvp blinky
