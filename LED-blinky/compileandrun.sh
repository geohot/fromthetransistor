#!/bin/bash

iverilog -o blinky blinky.v blinky_tb.v
vvp blinky
