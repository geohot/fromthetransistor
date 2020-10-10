from lexer import *
from mnemonics import Mnemonic
from conditions import condition_map

MAX_REGISTER_NUM = 11

def validate_register(register: str) -> None:
    reg_num = int(register[1:])

    if reg_num < 0 or reg_num > MAX_REGISTER_NUM:
        return Exception(f'register ${register} must be between 0-${MAX_REGISTER_NUM}')

    return None

def to_bin(num: int, bit_count: int) -> str:
    s = bin(num)[2:]
    for _ in range(bit_count - len(s)):
        s = '0' + s
    return s

def is_type(token_type, type) -> bool:
    return token_type == type

'''
1110 00 1 1101 0 0000 0010 000000000101 # mov r2, #5
____ _________ _ ____ ____ ____________
cond   inst    S 0000  Rd      imm12
'''

def assemble_mov_imm(tokens: [Token]) -> str:
    has_condition = is_type(tokens[1].token_type, TokenType.CONDITION)

    cond = condition_map[tokens[1].literal] if has_condition else condition_map['no']
    dest_reg = tokens[1].literal if not has_condition else tokens[2].literal
    error = validate_register(dest_reg)
    if not error == None:
        return error
    source_const = tokens[3].literal if not has_condition else tokens[4]
    return format_mov_imm(cond, int(dest_reg[1:]), int(source_const[1:]))

def format_mov_imm(cond: str, dest_reg: int, source_const: int) -> str:
    inst = '0011101'
    s = '0'
    rd = to_bin(dest_reg, 4)
    imm12 = to_bin(source_const, 12)
    
    return cond + inst + s + to_bin(0, 4) + rd + imm12

'''
1110 00 0 1101 0 0000 0010 00000000 0101 # mov r2, r5
____ _________ _ ____ ____ ________ ____
cond   inst    S  0s   Rd    0s      Rm 
'''
def assemble_mov_reg(tokens: [Token]) -> str:
    has_condition = is_type(tokens[1].token_type, TokenType.CONDITION)

    cond = condition_map[tokens[1].literal] if has_condition else condition_map['no']
    dest_reg = tokens[1].literal if not has_condition else tokens[2].literal
    error = validate_register(dest_reg)
    if not error == None:
        return error
    source_reg = tokens[3].literal if not has_condition else tokens[2].literal
    error = validate_register(source_reg)
    if not error == None:
        return error
    return format_mov_reg(cond, int(dest_reg[1:]), int(source_reg[1:]))

def format_mov_reg(cond: str, dest_reg: int, source_const: int) -> str:
    inst = '0001101'
    s = '0'
    rd = to_bin(dest_reg, 4)
    rm = to_bin(source_const, 4)
    
    return cond + inst + s + to_bin(0, 4) + rd + to_bin(0, 8) + rm

'''
1110 00 1 1010 1 0010 0000 000000000101 # cmp r2, #5
____ ___________ ____ ____ ____________
cond   inst       Rd  0000    imm12
'''
def assemble_cmp_imm(tokens: [Token]) -> str:
    has_condition = is_type(tokens[1].token_type, TokenType.CONDITION)

    cond = condition_map[tokens[1].token_type] if has_condition else condition_map['no']
    source_const = tokens[3].literal if not has_condition else tokens[4].literal
    dest_reg = tokens[1].literal if not has_condition else tokens[2].literal
    error = validate_register(dest_reg)
    if not error == None:
        return error
    return format_comp_imm(cond, int(dest_reg[1:]), int(source_const[1:]))

def format_comp_imm(cond: str, dest_reg: int, source_const: int) -> str:
    inst = '00110101'
    rn = to_bin(dest_reg, 4)
    imm12 = to_bin(source_const, 12)
    
    return cond + inst + rn + to_bin(0, 4) + imm12

'''
1110 010  1010 1 0010 0000 000000000101 
1110 010  0 0 0 0 1 0101        0010      000000000000 # cmp r2, #5
____ ___  _ _ _ _ _ ____        ____      ____________ 
cond inst P U 0 W 1 source reg  dest reg  offset
'''
def assemble_ldr_imm(tokens: [Token]) -> str:
    has_condition = is_type(tokens[1].token_type, TokenType.CONDITION)

    cond = condition_map[tokens[1].literal] if has_condition else condition_map['no']
    dest_reg = tokens[1].literal if not has_condition else tokens[2].literal
    error = validate_register(dest_reg)
    if not error == None:
        return error
    source_reg = tokens[3].literal if not has_condition else tokens[4].literal
    error = validate_register(source_reg)
    if not error == None:
        return error
    return format_ldr_imm(cond, int(dest_reg[1:]), int(source_reg[1:]))

def format_ldr_imm(cond: str, dest_reg: int, source_reg: int) -> str:
    inst = '010'
    P = '0'
    U = '0'
    W = '0'
    rt = to_bin(dest_reg, 4)
    rn = to_bin(source_reg, 4)
    imm12 = to_bin(0, 12)
    
    return cond + inst + P + U + '0' + W + '1' + rn + rt + imm12

'''
1110 0010100 0 0000 0000 000000000000
____ _______ _ ____ ____ ____________
cond inst    s rn   rd   imm
'''

def assemble_add_imm(tokens: [Token]) -> str:
    has_condition = is_type(tokens[1].token_type, TokenType.CONDITION)

    cond = condition_map[tokens[1].literal] if has_condition else condition_map['no']
    constant = tokens[5].literal if not has_condition else tokens[6].literal
    source_reg = tokens[1].literal if not has_condition else tokens[2].literal
    error = validate_register(source_reg)
    if not error == None:
        return error
    dest_reg = tokens[3].literal if not has_condition else tokens[4].literal
    error = validate_register(dest_reg)
    if not error == None:
        return error
    return format_add_imm(cond, int(dest_reg[1:]), int(source_reg[1:]), int(constant[1:]))

def format_add_imm(cond: str, dest_reg: int, source_reg: int, constant: int) -> str:
    inst = '0010100'
    s = '0'
    rn = to_bin(source_reg, 4)
    rd = to_bin(dest_reg, 4)
    imm12 = to_bin(constant, 12)

    return cond + inst + s + rn + rd + imm12

'''
1110 0010000 0 0000 0000 000000000000
____ _______ _ ____ ____ ____________
cond inst    s rn   rd   imm12
'''

def assemble_and_imm(tokens: [Token]) -> str:
    has_condition = is_type(tokens[1].literal, TokenType.CONDITION)

    cond = condition_map[tokens[1].literal] if has_condition else condition_map['no']
    constant = tokens[5].literal if not has_condition else tokens[6].literal
    source_reg = tokens[1].literal if not has_condition else tokens[2].literal
    error = validate_register(source_reg)
    if not error == None:
        return error
    dest_reg = tokens[3].literal if not has_condition else tokens[4].literal
    error = validate_register(dest_reg)
    if not error == None:
        return error
    
    return format_and_imm(cond, int(dest_reg[1:]), int(source_reg[1:]), int(constant[1:]))

def format_and_imm(cond: str, dest_reg: int, source_reg: int, constant: int):
    inst = '0010000'
    s = '0'
    rn = to_bin(source_reg, 4)
    rd = to_bin(dest_reg, 4)
    imm12 = to_bin(constant, 12)

    return cond + inst + s + rn + rd + imm12

'''
1110 010  0 0 0 0 0 0000 0000 000000000000
____ ___  _ _ _ _ _ ____ ____ ____________
cond inst p u 0 w 0 rn   rt   imm12
'''

def assemble_str_imm(tokens: [Token]) -> str:
    has_condition = is_type(tokens[1].literal, TokenType.CONDITION)

    cond = condition_map[tokens[1].literal] if has_condition else condition_map['no']
    constant = tokens[5].literal if not has_condition else tokens[6].literal
    source_reg = tokens[1].literal if not has_condition else tokens[2].literal
    error = validate_register(source_reg)
    if not error == None:
        return error
    dest_reg = tokens[3].literal if not has_condition else tokens[4].literal
    error = validate_register(dest_reg)
    if not error == None:
        return error
    
    return format_str_imm(cond, int(dest_reg[1:]), int(source_reg[1:]), int(constant[1:]))

def format_str_imm(cond: str, dest_reg: int, source_reg: int, constant: int) -> str:
    inst = '010'
    p = '0'
    u = '0'
    w = '0'
    rn = to_bin(source_reg, 4)
    rt = to_bin(dest_reg, 4)
    imm12 = to_bin(constant, 12)

    return cond + inst + p + u + '0' + w + '0' + rn + rt + imm12

'''
1101 1110 00000000
____ ____ ________
inst cond imm8
'''

def assemble_variable_number():
    pass

def format_variable_string():
    pass

def assemble_variable_string():
    pass

def assemble_branch(tokens: [Token]) -> str:
    has_condition = is_type(tokens[1].literal, TokenType.CONDITION)
    cond = condition_map[tokens[1].literal] if has_condition else condition_map['no']
    constant = tokens[1].literal if not has_condition else tokens[2].literal
    return format_branch(cond, int(constant[1:]))

def format_branch(cond: str, constant: int) -> str:
    inst = '1101'
    imm8 = to_bin(constant, 8)

    return inst + cond + imm8
