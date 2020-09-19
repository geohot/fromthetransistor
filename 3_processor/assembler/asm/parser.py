from lexer import *

MAX_REGISTER_NUM = 11

class Mnemonic:
    MOVE = "MOV"

# -> 32-bit binary number
# TODO: return binary number instead of str
def parse_instruction(tokens: [Token]) -> str:
    mnemonic = tokens[0] 
    if mnemonic == Mnemonic.MOVE:
       return parse_move(tokens)
        
# TODO: return binary number instead of str
def parse_move(tokens: [Token]) -> str:
    dest_register_token = tokens[1]
    source_token = tokens[2]

    if dest_register_token.token_type != TokenType.REGISTER:
        # TODO: wrap error with 'bad instruction' in parse_instruction.
        return Exception(f'bad instruction {tokens}. have destination token type {dest_register_token.token_type}, want {TokenType.REGISTER}')

    
    if source_token.token_type != TokenType.REGISTER and source_token.token_type != TokenType.CONSTANT:
        # TODO: wrap error with 'bad instruction' in parse_instruction.
        return Exception(f'bad instruction {tokens}. have source token type {source_token.token_type}, want {TokenType.REGISTER} or ${TokenType.CONSTANT}')

    validate_register(dest_register_token.literal)

    if source_token.token_type == TokenType.REGISTER:
        validate_register(source_token.literal)


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
