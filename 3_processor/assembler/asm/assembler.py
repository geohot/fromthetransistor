from lexer import *
from mnemonics import Mnemonic
from mnemonic_instructions import *

instruction_map = {
    (Mnemonic.MOVE.value, TokenType.REGISTER, TokenType.COMMA, TokenType.CONSTANT, TokenType.EOL): assemble_mov_imm,
    (Mnemonic.MOVE.value, TokenType.REGISTER, TokenType.COMMA, TokenType.REGISTER, TokenType.EOL): assemble_mov_reg,
    (Mnemonic.COMPARE.value, TokenType.REGISTER, TokenType.COMMA, TokenType.CONSTANT, TokenType.EOL): assemble_cmp_imm,
    (Mnemonic.LOAD.value, TokenType.REGISTER, TokenType.COMMA, TokenType.REGISTER, TokenType.EOL): assemble_ldr_imm
}

class Assembler:
    def __init__(self):
        self.binary_instructions = []
    
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
        if tokens[0].token_type == TokenType.MNEMONIC:
            key = tuple((tokens[0].literal, *map(lambda t: t.token_type, tokens[1:])))
            if key in instruction_map:
                return instruction_map[key](tokens)
        return Exception('Invalid instruction')
