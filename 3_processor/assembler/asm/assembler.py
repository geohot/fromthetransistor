from lexer import *
from mnemonics import Mnemonic
from mnemonic_instructions import *
from symbol_table import SymbolTable

instruction_map = {
    (Mnemonic.MOVE.value, TokenType.REGISTER, TokenType.COMMA, TokenType.CONSTANT, TokenType.EOL): assemble_mov_imm,
    (Mnemonic.MOVE.value, TokenType.REGISTER, TokenType.COMMA, TokenType.REGISTER, TokenType.EOL): assemble_mov_reg,
    (Mnemonic.COMPARE.value, TokenType.REGISTER, TokenType.COMMA, TokenType.CONSTANT, TokenType.EOL): assemble_cmp_imm,
    (Mnemonic.LOAD.value, TokenType.REGISTER, TokenType.COMMA, TokenType.REGISTER, TokenType.EOL): assemble_ldr_imm,
    (Mnemonic.ADD.value, TokenType.REGISTER, TokenType.COMMA, TokenType.REGISTER, TokenType.COMMA, TokenType.CONSTANT, TokenType.EOL): assemble_add_imm,
    (Mnemonic.AND.value, TokenType.REGISTER, TokenType.COMMA, TokenType.REGISTER, TokenType.COMMA, TokenType.CONSTANT, TokenType.EOL): assemble_and_imm,
    (Mnemonic.STR.value, TokenType.REGISTER, TokenType.COMMA, TokenType.REGISTER, TokenType.COMMA, TokenType.CONSTANT, TokenType.EOL): assemble_str_imm,
    (Mnemonic.B.value, TokenType.CONSTANT, TokenType.EOL): assemble_branch,
    (TokenType.VARIABLE_NAME, TokenType.VARIABLE_TYPE, TokenType.NUMBER): assemble_variable_number,
    (TokenType.VARIABLE_NAME, TokenType.VARIABLE_TYPE, TokenType.STRING): assemble_variable_string,
}

class Assembler:
    def __init__(self):
        self.binary_instructions = []
        self.symbol_table = SymbolTable()
    
    def assemble_instructions(self, tokens: [Token]) -> [str]:
        start = 0
        for i in range(1, len(tokens) + 1):
            if tokens[i - 1].literal == '\n':
                if i - start > 1:
                    self.binary_instructions.append(self.assemble_instruction(tokens[start:i]))
                    start = i
                else:
                    start = i
        return self.binary_instructions

    def assemble_instruction(self, tokens: [Token]) -> str:
        rest = tokens[2:] if len(tokens) > 1 and tokens[1].token_type == TokenType.CONDITION else tokens[1:]
        key = tuple((tokens[0].literal, *map(lambda t: t.token_type, rest))) if tokens[0].token_type == TokenType.MNEMONIC else tuple((map(lambda t: t.token_type, tokens)))
        print(key)
        if key in instruction_map:
            return instruction_map[key](tokens)

        return Exception('Invalid instruction')
