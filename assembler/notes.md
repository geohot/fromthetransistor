Notes
Stack pointer: points to top of stack.
every memory address holds a byte
```
0x01 n
0x02 s
0x03 fourth <- top of stack
0x04 third
0x05 second
0x05 first
high adress -> low address
```

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

Current Program Status Register (CPSR): Holds state of last excecution.
Example: wether there was a carry bit, negative value, if we're in privileged mode, ...

ARM VS Thumb (arm state)
ARM:
- Instructions are 32-bit
- Conditional execution
- Barrel shifter: shrinks multiple instructions into one
Thumb:
- Usuually instructions are 16-bit, can be 32-bit if need be.
- Conditional execution by using `IT` instructions (only available on some archs)
- Useful for exploits, because there's less NULL bytes. Example. 8 = 0000 0000 0000 1000 in 32 bit, 0000 1000 in 16-bit.

Notes
When reading PC while debugging, PC will point to two instructions ahead. This is old behavior that is maintained to ensure compatability.
Carry occurs if result of a subtraction is >= 0

Program counter: current instruction memory address plus word length (8 in a 32-bit arch)
during branch: holds destination address

Questions:

What's up with arm storing first four argruments of a function in first four registers? Only four arguments can be stored at a time? Is a functino an arm instruction?


Building assembler:
assembly file -> assembler -> machine code
1. Parse each instruction into an operator, register, memory address, etc
2. Map each instruction into machine code for armv6
  Map each operator into machine code
  Map each register into machine code
  Map each memory address into machine code
```
mov r0, #5 -> 0101010101....
```
How do we get each instruction's machine code?



