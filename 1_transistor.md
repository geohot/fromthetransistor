# Section 1: Intro: Cheating our way past the transistor -- 0.5 weeks
## Transistors
*What is a transistor?*
History - Before the transistor
**Vaccum tubes**
  - Use heat turn circuits on or off

**silicon**
  - semiconductor: conducts electricity on some conditions; makes easy to turn circuit on and off.
  - will form covalent bonds with other silicon atoms

**Integrated circuits**
  - by adding Phosphorus (has extra electron) to a group of silicon atoms, we create a negative charge, since extra electron is bouncing through group of silicon atoms; phosphorus -> **negative charge**
  - by adding Boron (wants electron), to a group of silicon atoms, we create a whole, since silicon atoms will steal electrons from other silicon atoms constantly; **boron -> positive charge**

**Bipolar junction transistor**
- NPN type transistor (negative/positive)
    - Three areas: N Type, then P type, then N type.
    - excess electrons in N areas will move to P area, preventing current from flowing
    - if positive voltage is added: electrons will flow through the circuit

**Boolean logic**
  - Integrated circuits can be used to represent information
  - Each transistor can be on or off, we can use boolean gates to create additions, and conditional logic (ex AND, OR, XOR)

**Transistors**
  - composed of integrated circuits
*What are FPGAs?*
Field Programmable Gate Array
- Closest you can get to designing your own chip
- Design digital functions
- Can turn into any microcontroller: digital siganl processor, progam LEDs, etc
- Composed of 10s of thousands of (or more) **CLBS** for hobbby FPBGAs
- **CLBS** can be programmed with HDL or Verilog

**CLB**
- Configurable Logic Block
- Can implement any digital function
- More complex than Gates 
- contain **Flip flops** and **LUTs**
- flexible inputs

**Lookup table**
- 4 inputs or more
- programmable

**Flip flops**
- 1 or more flip flops in a CLB
- Latched and clocked logic

*FPGAs vs Microcontrollers*

*Describe how FPGAs are buildable using transistors.*

*What are Integrated Circuits?*

*What are LUTs?*

*Talk briefly about the theory of transistors*

## Emulation
Building on real hardware limits the reach of this course. Using something like Verilator will allow anyone with a computer to play
Verilator
    Tasks:
    - [ ] 
