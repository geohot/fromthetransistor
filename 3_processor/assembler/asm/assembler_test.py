from lexer import Lexer
from assembler import Assembler

correct_instructions = [
    '0000 00 1 1101 0 0000 0001 000000000111',
    '0000 00 0 1101 0 0000 0010 000000000101',
    '0000 00 1 1010 1 0010 0000 000000000101',
    '0000 010 0 0 0 0 1 0101 0010 000000000000',
]

asm_source_code = '''
mov r1, #7
mov r2, r5
cmp r2, #5
ldr r2, r5
'''

def test():
    lexer = Lexer()
    assembler = Assembler()
    
    bin_instructions = assembler.assemble_instructions(lexer.tokenize_instructions(asm_source_code))

    print("look at my binaries")
    print(bin_instructions)

    if len(bin_instructions) != len(correct_instructions):
        print(f'have bin instruction len {len(bin_instructions)}, want {len(correct_instructions)}')
        exit()

    for i in range(len(bin_instructions)):
        bin_inst = bin_instructions[i] 
        correct_bin_inst = correct_instructions[i].replace(' ', '')
        if bin_inst != correct_bin_inst:
            print(f'have bin instruction {bin_inst}, want {correct_bin_inst}')
            exit()
    print("good binaries, thank you")

test()
