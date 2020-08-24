#include "Vhello.h"
#include "verilated.h"

int main(int argc, char** argv, char** env) {
    Verilated::commandArgs(argc, argv);
    Vhello* top = new Vhello;
    while (!Verilated::gotFinish()) { top->eval(); }
    delete top;
    exit(0);
}