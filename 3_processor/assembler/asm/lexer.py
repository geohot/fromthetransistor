import os
import enum 
import sys
from mnemonics import mnemonic_literals

class TokenType(enum.Enum):
    MNEMONIC = enum.auto()
    COMMA = enum.auto()
    REGISTER = enum.auto()
    CONSTANT = enum.auto()
    ILLEGAL = enum.auto()
    EOL = enum.auto()

    def __str__(self):
        return self.name

class Token:
    def __init__(self, token_type: TokenType, literal: str):
        self.token_type = token_type
        self.literal = literal

    def __str__(self):
        return "token_type: " + self.token_type.__str__() + ", literal: " + self.literal.__str__()

class Lexer:
    def __init__(self):
        self.tokens = []
        self.current = 0

    def is_digit(self, string: str) -> bool:
        try:
            int(string)
            return True
        except:
            return False

    def is_whitespace(self, char: str) -> bool:
        return char == " "

    def tokenize_instructions(self, input_text: str) -> [[Token]]:
        for line in input_text.splitlines():
            while self.current < len(line):
                if not self.is_whitespace(line[self.current]): 
                    self.tokens.append(self.next_token(line, len(line)))
                self.current += 1
            self.tokens.append(Token(TokenType.EOL, "\n"))
            self.current = 0

        return self.tokens

    def next_token(self, input_text: str, end: int) -> Token:
        start = self.current
        while self.current < end:
            if self.is_whitespace(input_text[self.current]):
                return Token(self.token_type(input_text[start:self.current]), input_text[start:self.current])
            elif self.current + 1 < end and input_text[self.current + 1] == ',':
                return Token(self.token_type(input_text[start:self.current + 1]), input_text[start:self.current + 1])
            self.current += 1
        return Token(self.token_type(input_text[start:self.current]), input_text[start:self.current])

    def token_type(self, literal: str) -> TokenType:
        if literal == ',':
            return TokenType.COMMA
        if literal in mnemonic_literals:
            return TokenType.MNEMONIC
        if len(literal) > 1:
            if literal[0] == 'r' and self.is_digit(literal[1:]):
                return TokenType.REGISTER
            elif literal[0] == '#':
                return TokenType.CONSTANT
        return TokenType.ILLEGAL

