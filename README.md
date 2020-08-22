# From the Transistor to the Web Browser

Hiring is hard, a lot of modern CS education is really bad, and it's hard to find people who understand the modern computer stack from first principles.

Now cleaned up and going to be software only. Closer to being real.

## Section 1: Intro: Cheating our way past the transistor -- 0.5 weeks
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
- made out of p-n junctions - borders between two materials with different charges on them  

**Electricity** - the motion of electrons through charged semiconductant materials - in this case, silicon  

**Silicon** - semiconductor with 4 electrons on its outer energy level; is able to form a stable crystal lattice made of four-way covalent bonds when not altered

**Diodes** - Allows current to flow in one direction if a certain voltage is reached. Consists of *anode*, depletion layer *cathode*  
  **Anode** - P-doped (positive) side of junction  
  **Depletion layer** - Emerges where the excess electrons from the cathode and holes from the anode meet, creating a layer depleted of charge.  
  **Cathode** - N-doped (negative) side of junction  
  **Reverse Bias** - when positive voltage is applied to n-doped side and negative voltage is applied to positive side, it increases the dead zone layer and prevents the flow of current  
  **Forward Bias** - if positive voltage is added to positive side and negative voltage is added to negative side: electrons will flow through the circuit  

**Doping Silicon - Introducing Charge**  
- replacing silicon atoms with phosphorous atoms in a matrix of silicon atoms introduces a negative charge since extra electrons are bouncing through the group of silicon atoms; **phosphorous -> negative charge**  
- replacing silicon atoms with boron atoms in a matrix of silicon atoms creates "holes" (missing electrons), introducing a positive charge in the silicon plate; **boron -> positive charge**  

**Depletion Layer / Dead Zone**  
- when p-doped and n-doped silicon plates meet, the junction between the plates will form a "barrier" where the extra electrons from the n-doped plate join the holes from the p-doped plate; this area has no charge  
- when large enough, the dead zone effectively blocks the flow of electrons crossing the p-n junction, preventing the flow of electricity  
- can be manipulated in size by applying differently charged voltages to the p-doped and n-doped plates  

**NPN Bipolar junction transistor type transistor**  
- Three areas: N Type (side 1), then P Type (side 2), then N type (side 3); the sides of the P type (side 2) form depletion layers between it and the N types  
- When a negative voltage is applied to side 1 (N type), then it causes the depletion layer between side 1 and side 2 to be larger (electrons are "pushed" towards the holes, causing more holes to fill up), which reduces the second depletion layer due to a larger attraction with the side with the negative voltage  
- When a positive voltage is then applied to side 2 (P type), electrons will begin to cross because the second depletion layer is small enough for electrons to jump it  
- Thus, you need two voltages; a negative one to side 1 or 3, and a positive one to side 2  

### Integrated Circuits  
**What are Integrated Circuits?** - Very small complete circuit, made out of silicon  

**How are Integrated Circuits made?**  
1. **create Wafer** - Slice a cylinder of silicon to create a wafer  
2. **Masking** - Add protective layer called **photoresist** to all of wafer  
3. **Etching** - Remove **photoresist** from some parts of silicon  
4. **Doping** - Introduce impurities into the etched parts of silicon. This can be done by heating up the wafer, or blasting positively and negetively charged atoms onto it. This will create n-doped junctions and p-doped junctions.  

**Boolean logic** - Math. function with binary input, binary output. Ex: fn = AND(one: 0|1, two: 0|1) -> out: 0|1  
**Logic gates** Implementation of boolean logic, usually with transistors. Transistors can act as switches, which can be on or off. We can use boolean gates to create boolean logic (ex AND, OR, XOR).  

**FPGA - Field Programmable Gate Array**
- Closest you can get to designing your own chip  
- Design digital functions by programming the hardware using an HDL like Verilog  
- Can be used (theoretically, not practically) in place of any microcontroller: digital siganl processor, progam LEDs, etc  
- Composed of 10s of thousands of (or more) **CLBS** for hobbby FPBGAs; in those CLBS are many Logic Blocks  

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

### Emulation
Building on real hardware limits the reach of this course. Using something like Verilator will allow anyone with a computer to play

## Section 2: Bringup: What language is hardware coded in? -- 0.5 weeks
- Blinking an LED(Verilog, 10) -- Your first little program! Getting the simulator working. Learning Verilog.
- Building a UART(Verilog, 100) -- An intro chapter to Verilog, copy a real UART, introducingsubchapters the concept of MMIO, though the serial port may be semihosting. Serial test echo program and led control.

## Section 3: Processor: What is a processor anyway? -- 3 weeks
- Coding an assembler(Python, 500) -- Straightforward and boring, write in python. Happens in parallel with the CPU building. Teaches you ARM assembly. Initially outputs just binary files, but changed when you write a linker.
- Building a ARM7 CPU(Verilog, 1500) -- Break this into subchapters. A simple pipeline to start, decode, fetch, execute. How much BRAM do we have? We need at least 1MB, DDR would be hard I think, maybe an SRAM. Simulatable and synthesizable.
- Coding a bootrom(Assembler, 40) -- This allows code download into RAM over the serial port, and is baked into the FPGA image. Cute test programs run on this.

## Section 4: Compiler: A “high” level language -- 3 weeks
- Building a C compiler(Haskell, 2000) -- A bit more interesting, cover the basics of compiler design. Write in haskell. Write a parser. Break this into subchapters. Outputs ARM assembly.
- Building a linker(Python, 300) -- If you are clever, this should take a day. Output elf files. Use for testing with QEMU, semihosting.
- libc + malloc(C, 500) -- The gateway to more complicated programs. libc is only half here, things like memcpy and memset and printf, but no syscall wrappers.
- Building an ethernet controller(Verilog, 200) -- Talk to a real PHY, consider carefully MMIO design.
- Writing a bootloader(C, 300) -- Write ethernet program to boot kernel over UDP. First thing written in C. Maybe don’t redownload over serial each time and embed in FPGA image.

## Section 5: Operating System: Software we take for granted -- 3 weeks
- Building an MMU(Verilog, 1000) -- ARM9ish, explain TLBs and other fun things. Maybe also a memory controller, depending on how the FPGA is, then add the init code to your bootloader.
- Building an operating system(C, 2500) -- UNIXish, only user space threads. (open, read, write, close), (fork, execve, wait, sleep, exit), (mmap, munmap, mprotect). Consider the debug interface you are using, ranging from printf to perhaps a gdbremote stub into kernel. Break into subchapters.
- Talking to an SD card(Verilog, 150) -- The last hardware you have to do. And a driver
- FAT(C, 300) -- A real filesystem, I think fat is the simplest
- init, shell, download, cat, ls, rm(C, 250) -- Your first user space programs.

## Section 6: Browser: Coming online -- 1 week
- Building a TCP stack(C, 500) -- Probably coded in the kernel, integrate the ethernet driver into the kernel. Add support for networking syscalls to kernel. (send, recv, bind, connect)
- telnetd, the power of being multiprocess(C, 50) --  Written in C, user can connect multiple times with telnet. Really just a bind shell.
- Space saving dynamic linking(C, 300) -- Because we can, explain how dynamic linker is just a user space program. Changes to linker required.
- So about that web(C, 500+) -- A “nice” text based web browser, using ANSI and terminal niceness. Dynamically linked and nice, nice as you want.

## Section 7: Physical: Running on real hardware -- 1 week
- Talking to an FPGA(C, 200) -- A little code for the USB MCU to bitbang JTAG.
- Building an FPGA board -- Board design, FPGA BGA reflow, FPGA flash, a 50mhz clock, a USB JTAG port and flasher(no special hardware, a little cypress usb mcu to do jtag), a few leds, a reset button, a serial port(USB-FTDI) also powering via USB, an sd card, expansion connector(ide cable?), and an ethernet port. Optional, expansion board, host USB port, NTSC TV out, an ISA port, and PS/2 connector on the board to taunt you. We provide a toaster oven and a multimeter thermometer to do reflow. 
- Bringup -- Compiling and downloading the Verilog for the board
