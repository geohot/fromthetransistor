from lexer import *
from mnemonics import Mnemonic
from mnemonic_instructions import *

def assemble_instructions(instructions):
    binary_instructions = []
    for instruction in instructions:
        if len(instruction) == 1 and instruction[0].token_type == TokenType.EOL:
            continue
        binary_instruction = assemble_instruction(instruction) # 32-bit binary number
        binary_instructions.append(binary_instruction)
    return binary_instructions

# -> 32-bit binary number
def assemble_instruction(fields: [Token]) -> str:
    if fields[0].token_type == TokenType.MNEMONIC:
        (fields_tuple, literals) = get_mnemo_instruction_fields_and_literals(fields)
        if fields_tuple not in mnemonic_assemble_func:
            return Exception('Invalid instruction')
        assemble_func = mnemonic_assemble_func[fields_tuple]
        return assemble_func(*literals)
    return Exception('Invalid instruction')

def get_mnemo_instruction_fields_and_literals(fields: [Token]) -> tuple:
    if len(fields) < 4:
        return Exception(f'have {len(fields)} tokens for mnemonic instruction, want at least 4')
    if fields[0].token_type != TokenType.MNEMONIC:
        return Exception(f'have first token type: {fields[0].token_type}, want {TokenType.Mnemonic}')
    if fields[2].token_type != TokenType.COMMA:
        return Exception(f'have third token type: {fields[2].token_type}, want {TokenType.COMMA}')
    if fields[3].token_type != TokenType.ILLEGAL:
        return Exception(f'have fourth token type: {fields[2].token_type}, want {TokenType.ILLEGAL}')

    mnemo = fields[0].literal
    left_literal = fields[1].literal 
    left_type = fields[1].token_type 
    after_comma_types = list(map(lambda t: t.token_type, fields[4:len(fields)-1]))
    after_comma_literals = list(map(lambda t: t.literal, fields[4:len(fields)-1]))

    field_tuple = tuple([mnemo, left_type] + after_comma_types)
    literals = tuple([left_literal] + after_comma_literals)

    return (field_tuple, literals)

MAX_REGISTER_NUM = 11
def validate_register(register: str) -> None:
    err = Exception(f'register ${register} must be between 0-${MAX_REGISTER_NUM}')

    reg_num = 0
    try:
        reg_num = int(register[1:])
    except:
        return err

    if reg_num < 0 or reg_num > MAX_REGISTER_NUM:
        return err

    return None
