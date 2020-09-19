## Section 3: Processor: What is a processor anyway? -- 3 weeks
- Coding an assembler(Python, 500) -- Straightforward and boring, write in python. Happens in parallel with the CPU building. Teaches you ARM assembly. Initially outputs just binary files, but changed when you write a linker.
- Building a ARM7 CPU(Verilog, 1500) -- Break this into subchapters. A simple pipeline to start, decode, fetch, execute. How much BRAM do we have? We need at least 1MB, DDR would be hard I think, maybe an SRAM. Simulatable and synthesizable.
- Coding a bootrom(Assembler, 40) -- This allows code download into RAM over the serial port, and is baked into the FPGA image. Cute test programs run on this.
