// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Design implementation internals
// See Vhello.h for the primary calling header

#include "Vhello.h"
#include "Vhello__Syms.h"

//==========

VL_CTOR_IMP(Vhello) {
    Vhello__Syms* __restrict vlSymsp = __VlSymsp = new Vhello__Syms(this, name());
    Vhello* const __restrict vlTOPp VL_ATTR_UNUSED = vlSymsp->TOPp;
    // Reset internal values
    
    // Reset structure values
    _ctor_var_reset();
}

void Vhello::__Vconfigure(Vhello__Syms* vlSymsp, bool first) {
    if (false && first) {}  // Prevent unused
    this->__VlSymsp = vlSymsp;
    if (false && this->__VlSymsp) {}  // Prevent unused
    Verilated::timeunit(-12);
    Verilated::timeprecision(-12);
}

Vhello::~Vhello() {
    VL_DO_CLEAR(delete __VlSymsp, __VlSymsp = NULL);
}

void Vhello::_initial__TOP__1(Vhello__Syms* __restrict vlSymsp) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vhello::_initial__TOP__1\n"); );
    Vhello* const __restrict vlTOPp VL_ATTR_UNUSED = vlSymsp->TOPp;
    // Body
    VL_WRITEF("Hello World\n");
    VL_FINISH_MT("hello.v", 2, "");
}

void Vhello::_eval_initial(Vhello__Syms* __restrict vlSymsp) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vhello::_eval_initial\n"); );
    Vhello* const __restrict vlTOPp VL_ATTR_UNUSED = vlSymsp->TOPp;
    // Body
    vlTOPp->_initial__TOP__1(vlSymsp);
}

void Vhello::final() {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vhello::final\n"); );
    // Variables
    Vhello__Syms* __restrict vlSymsp = this->__VlSymsp;
    Vhello* const __restrict vlTOPp VL_ATTR_UNUSED = vlSymsp->TOPp;
}

void Vhello::_eval_settle(Vhello__Syms* __restrict vlSymsp) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vhello::_eval_settle\n"); );
    Vhello* const __restrict vlTOPp VL_ATTR_UNUSED = vlSymsp->TOPp;
}

void Vhello::_ctor_var_reset() {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vhello::_ctor_var_reset\n"); );
}
