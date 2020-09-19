### Transistors
*What is a transistor?* *Talk briefly about the theory of transistors*

**Reference Links**    
Transistor Theory - https://backyardbrains.com/experiments/transistorTheory#prettyPhoto  
Transistor Circuit Design - https://backyardbrains.com/experiments/transistorDesign  

**History - Before the transistor**  
**Vaccum tubes**  
- use heat turn circuits on or of  

**Transistors**  
- the "atoms" of integrated circuits  
- used as *switches* or amplifiers to electrical currents  
- made out of p-n junctions - the border between p-doped and n-doped silicon

**Electricity** - the motion of electrons through charged semiconductant materials

**Silicon** - semiconductor with 4 electrons on its outer energy level; is able to form a stable crystal lattice made of four-way covalent bonds when not altered

**Diodes** - Allows current to flow in one direction if a certain voltage is reached. Consists of an *anode* and a *cathode*  
  **Anode** - P-doped (positive) side of junction  
  **Depletion layer** - Emerges where the excess electrons from the cathode and holes from the anode meet, creating a layer depleted of charge; can be altered in size 
  **Cathode** - N-doped (negative) side of junction  
  **Reverse Bias** - when electric current is prevented from flowing through the diode, making an insulator out of the diode
  **Forward Bias** - when electric current can flow freely through the circut

**Doping Silicon - Introducing Charge**  
- replacing silicon atoms with phosphorous atoms in a matrix of silicon atoms introduces a negative charge since extra electrons are bouncing through the group of silicon atoms; **phosphorous -> negative charge**  
- replacing silicon atoms with boron atoms in a matrix of silicon atoms creates "holes" (missing electrons), introducing a positive charge in the silicon plate; **boron -> positive charge**  

**Depletion Layer / Dead Zone**  
- emerges when excess electrons from the cathode and holes from the anode meet, creating a layer depleted of charge
- when large enough, the dead zone effectively blocks the flow of electrons crossing the p-n junction, preventing the flow of electricity  
- can be manipulated in size by applying different voltages to the p-doped and n-doped plates  

**NPN Bipolar junction transistor type transistor**  
- N: n-doped layer, P: p-doped layer; two n-p junctions
- A forward bias on one n-p junction will natrually cause a reverse bias on the other n-p junction; this leads to you needing a second voltage applied for current to flow

### Integrated Circuits  
**What are Integrated Circuits?** - Very small circuits made from other smaller circuits made out of discrete logic components made out of silicon  

**How are Integrated Circuits made?**  
1. **create Wafer** - Slice a cylinder of silicon to create a wafer  
2. **Masking** - Add protective layer called **photoresist** to all of wafer  
3. **Etching** - Remove **photoresist** from some parts of silicon  
4. **Doping** - Introduce impurities into the etched parts of silicon. This can be done by heating up the wafer, or blasting positively and negetively charged atoms onto it. This will create n-doped junctions and p-doped junctions.  

**Boolean logic** - Math? Function with binary input, binary output. Ex: fn = AND(one: 0|1, two: 0|1) -> out: 0|1  
**Logic gates** Implementation of boolean logic from discrete logic units (transistors and such). Transistors can act as switches, which can be on or off. We can use boolean gates to create boolean logic (ex AND, OR, XOR).  

**FPGA - Field Programmable Gate Array**
- "programmable hardware"; you can configure digital logic that will run on actual hardware (LUTS, Switches, FlipFlops, and BRAM)
- Design digital functions by programming the hardware using an HDL like Verilog or VHDL; helpful note: not programming languages
- Composed of 10s of thousands of (or more) **CLBS** for hobbby FPBGAs; in those CLBS are many Logic Blocks, signals are routed using the Interconnected Matrix which sounds like a matrix of wires that allow signals to be routed to Logic Blocks through Switches (latches?); inputs and outputs can be "programmed" or configured in the LUT acting like a Truth Table that simulates practically any function with the same number of inputs and outputs; signals can be then routed anywhere within the FPGA

**CLB - Configurable Logic Block**
- More complex than Gates because they can implement any digital function, have flexible inputs  
- Can be programmed with HDL or Verilog  
- Contain a few *logic cells*  

**Logic cell** - Contains *Flip flops*, a *full-adder* and *LUTs*  

**Full-adder** - Takes in two binary inputs, each one bit, and a carry input, outputs the sum of the binary inputs, and the carry bit.  

**LUTs - Lookup tables** - Implentation of Boolean Gates (AND|OR|...) using muxes that act as truth tables. We hardcode the output for specific inputs.  

**Register/Flip flop** - Record the value of input every clock cycle. Used to "record" state.  

**Microcontroller**
- CPU
- memory (in memory cells within a IC chip)
- programmable I/O
- sometimes a little RAM
- insignificant power consumption when off

