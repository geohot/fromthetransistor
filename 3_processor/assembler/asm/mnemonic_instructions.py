from lexer import *
from mnemonics import Mnemonic

'''
0000 00 1 1101 0 0000 0010 000000000101 # mov r2, #5
____ _________ _ ____ ____ ____________
cond   inst    S 0000  Rd      imm12
'''

def assemble_mov_imm(dest_reg: str, source_const: str) -> str:
    return format_mov_imm(int(dest_reg[1:]), int(source_const[1:]))

def format_mov_imm(dest_reg: int, source_const: int) -> str:
    cond = '0000'
    inst = '0011101'
    s = '0'
    rd = to_bin(dest_reg, 4)
    imm12 = to_bin(source_const, 12)
    
    return cond + inst + s + to_bin(0, 4) + rd + imm12

'''
0000 00 0 1101 0 0000 0010 00000000 0101 # mov r2, r5
____ _________ _ ____ ____ ________ ____
cond   inst    S  0s   Rd    0s      Rm 
'''
def assemble_mov_reg(dest_reg: str, source_reg: str) -> str:
    return format_mov_reg(int(dest_reg[1:]), int(source_reg[1:]))

def format_mov_reg(dest_reg: int, source_const: int) -> str:
    cond = '0000'
    inst = '0001101'
    s = '0'
    rd = to_bin(dest_reg, 4)
    rm = to_bin(source_const, 4)
    
    return cond + inst + s + to_bin(0, 4) + rd + to_bin(0, 8) + rm

'''
0000 00 1 1010 1 0010 0000 000000000101 # cmp r2, #5
____ ___________ ____ ____ ____________
cond   inst       Rd  0000    imm12
'''
def assemble_cmp_imm(dest_reg: str, source_const: str) -> str:
    return format_comp_imm(int(dest_reg[1:]), int(source_const[1:]))

def format_comp_imm(dest_reg: int, source_const: int) -> str:
    cond = '0000'
    inst = '00110101'
    rn = to_bin(dest_reg, 4)
    imm12 = to_bin(source_const, 12)
    
    return cond + inst + rn + to_bin(0, 4) + imm12

'''
0000 010  1010 1 0010 0000 000000000101 
0000 010  0 0 0 0 1 0101        0010      000000000000 # cmp r2, #5
____ ___  _ _ _ _ _ ____        ____      ____________ 
cond inst P U 0 W 1 source reg  dest reg  offset
'''
def assemble_ldr_imm(dest_reg: str, source_reg: str) -> str:
    return format_ldr_imm(int(dest_reg[1:]), int(source_reg[1:]))

def format_ldr_imm(dest_reg: int, source_reg: int) -> str:
    cond = '0000'
    inst = '010'
    P = '0'
    U = '0'
    W = '0'
    rt = to_bin(dest_reg, 4)
    rn = to_bin(source_reg, 4)
    imm12 = to_bin(0, 12)
    
    return cond + inst + P + U + '0' + W + '1' + rn + rt + imm12
        
mnemonic_assemble_func = { 
    (Mnemonic.MOVE.value, TokenType.REGISTER, TokenType.REGISTER): assemble_mov_reg,
    (Mnemonic.MOVE.value, TokenType.REGISTER, TokenType.CONSTANT): assemble_mov_imm,
    (Mnemonic.COMPARE.value, TokenType.REGISTER, TokenType.CONSTANT): assemble_cmp_imm,
    (Mnemonic.LOAD.value, TokenType.REGISTER, TokenType.REGISTER): assemble_ldr_imm,
}

def to_bin(num: int, bit_count: int) -> str:
    s = bin(num)[2:]
    for _ in range(bit_count - len(s)):
        s = '0' + s
    return s

