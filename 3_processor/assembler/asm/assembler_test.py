from lexer import *
from assembler import *

want_bin_instructions = [
    '0000 00 1 1101 0 0000 0001 000000000111',
    '0000 00 0 1101 0 0000 0010 000000000101',
    '0000 00 1 1010 1 0010 0000 000000000101',
    '0000 010 0 0 0 0 1 0101 0010 000000000000',
]

file_text = '''
mov r1, #7
mov r2, r5
cmp r2, #5
ldr r2, r5
'''

def test():
    instructions_fields = tokenize_instructions(file_text)
    bin_instructions = assemble_instructions(instructions_fields)

    print("look at my binaries")
    print(bin_instructions)

    if len(bin_instructions) != len(want_bin_instructions):
        print(f'have bin instruction len {len(bin_instructions)}, want {len(want_bin_instructions)}')
        exit()

    for i in range(len(bin_instructions)):
        bin_inst = bin_instructions[i] 
        want_bin_inst = want_bin_instructions[i].replace(' ', '')
        if bin_inst != want_bin_inst:
            print(f'have bin instruction {bin_inst}, want {want_bin_inst}')
            exit()
    print("good binaries, thank you")

test()
