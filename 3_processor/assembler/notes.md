# Assembler notes

## Assembly

### Stack
Stack pointer: points to top of stack.
every memory address holds a byte
```
0x01 n
0x02 s
0x03 fourth <- top of stack
0x04 third
0x05 second
0x05 first

stack grows from high address, to lower address
```

### Link register
Link register: parent function memory address
example:

with function calls:
```
a()
b()
c()
```
corresponding lrs
```
a()
lr = b

b()
lr = c

c()
```

### CPSR
Current Program Status Register (CPSR): Holds state of last excecution.
Example: wether there was a carry bit, negative value, if we're in privileged mode, ...

### ARM vs Thumb
ARM VS Thumb (arm state)
ARM:
- Instructions are 32-bit
- Conditional execution
- Barrel shifter: shrinks multiple instructions into one
Thumb:
- Usuually instructions are 16-bit, can be 32-bit if need be.
- Conditional execution by using `IT` instructions (only available on some archs)
- Useful for exploits, because there's less NULL bytes. Example. 8 = 0000 0000 0000 1000 in 32 bit, 0000 1000 in 16-bit.

### Notes while programming
When reading PC while debugging, PC will point to two instructions ahead. This is old behavior that is maintained to ensure compatability.
Carry occurs if result of a subtraction is >= 0

Program counter: current instruction memory address plus word length (8 in a 32-bit arch)
during branch: holds destination address

#### Questions:

What's up with arm storing first four argruments of a function in first four registers? Only four arguments can be stored at a time? Is a functino an arm instruction?

---
## Building assembler:
Assembler: assembly file -> assembler -> machine code
1. Parse each instruction into an operator, register, memory address, etc
2. Map each instruction into machine code for armv6
  - Map each operator into machine code
  - Map each register into machine code
  - Map each memory address into machine code

Example:
```
mov r0, #5 -> 0101010101....
```

### Machine languages
``` 
Binary:         10101011 10101111 000001010110010010 # Numbers depend on ARM asm spec 
                ________|________|________________
Symbolic (asm): LOAD     R3       7
```

### Symbols
Symbol = Variable | Label | pre-defined symbol (operator, mnemonic, registers)
Each symbol is mapped to a memory address specified in Symbol Table

Label: maps to next intruction memory adderss
Variable: each new variable assembler looks at gets assigned higher memory address

### Binary code file:
a 32-bit instruction in every line

Instructions:
A-instruction
B-instruction

Example:
```
01011100010111000101110001011100
01011100010111000101110001011100
```

### ELF (Executable Linux File)
Includes necessary headers, metadata, and binary program to execute. We need to turn a machine-code file into an ELF file to be able to execute it.

#### Questions
*How does the asm know which memory address a pre-defined symbol (mnemonic/register/operator) belongs to?*
The assembly spec (ARMv7 spec) speficies a number for every pre-defined symbol. These values are initiliazed when the assembler start
```
hypothetical symbol table
-----------
mov | 0x1
add | 0x2
sub | 0x3
 ...  |
```

*How does the asm know which memory address a label belongs to?*
In the first pass, the asm maps the label name, to the next instruction memory address in the Symbolic Table
Example
```
label: 0x0
  add 5, 2 0x1

symbol table
-----------
label | 0x1
 ...  |
```

*How does the asm know which memory address a variable belongs to?*
In the first pass, the asm looks for variable declarations, and maps a memory address for it in the Symbolic Table. In the second pass, asm replaces all variables with memory address in Symbolic Table.
Example
```
var1= 0
var2= 0

symbol table
-----------
var1  | 1024
var2  | 1025
 ...  |
```

### Assember pseudo-code
```
def assembler:
  bin_instructions = []

  for line in file: #line is a command (or whitespace/comment)
    fields = parse_fields(line) # 'LOAD r1, 7' -> [LOAD, r1, 7]

    command_bin_codes = []
    for field in fields:
      bin_code = field_binary_code(field) # LOAD -> 0101010110
      cmd_bin_codes.add(bin_code)
    cmd_bin_instructions = parse_bin_codes(command_bin_codes) #list of 32-bit binaries
    bin_instructions.add(cmd_bin_instructions)

  asm_bin_instructions = assemble_bin_codes(bin_instructions)
  file.write('asm.o', asm_bin_instructions)
```

Implmentation overview:
- [X] parse source code into commands
- [ ] parse commands into instruction fields
  - [ ] parse a instruction
  - [ ] parse b instruction
- [ ] map instruction field into binary number
- [ ] create binary instruction from binary fields numbers
- [ ] add instruction binary to output file
