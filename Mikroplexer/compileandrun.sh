echo "compiling..";
iverilog -o testbench.vvp microplexer_tb.v
echo "running..";
echo
echo "output:"
vvp testbench.vvp
