import os
import enum 
import sys
from mnemonics import mnemonic_literals
from conditions import condition_literals

class TokenType(enum.Enum):
    MNEMONIC = enum.auto()
    COMMA = enum.auto()
    REGISTER = enum.auto()
    CONSTANT = enum.auto()
    CONDITION = enum.auto()
    ILLEGAL = enum.auto()
    VARIABLE_REFERENCE = enum.auto()
    VARIABLE_NAME = enum.auto()
    VARIABLE_TYPE = enum.auto()
    STRING = enum.auto()
    NUMBER = enum.auto()
    EOL = enum.auto()

    def __str__(self):
        return self.name

class Token:
    def __init__(self, token_type: TokenType=TokenType.ILLEGAL, literal: str=''):
        self.token_type = token_type
        self.literal = literal

    def __str__(self):
        return "<Token(token_type= " + str(self.token_type) + ", literal= " + self.literal + ")>"

    def __repr__(self):
        return self.__str__()

class Lexer:
    def __init__(self, symbol_table):
        self.tokens = []
        self.current = 0
        self.symbol_table = symbol_table

    def is_digit(self, string: str) -> bool:
        try:
            int(string)
            return True
        except:
            return False

    def is_whitespace(self, char: str) -> bool:
        return char == " "

    def initialize_symbol_table(self, input_text) -> None:
        current_instruction = 0
        tokens = self.tokenize_instructions(input_text)
        for i in range(0, len(tokens)):
            token = tokens[i]
            if token.token_type == TokenType.VARIABLE_NAME:
                next_token = tokens[i + 1]
                if next_token.token_type == TokenType.EOL:
                    current_instruction -= 1
                    self.symbol_table.add_label(token.literal, current_instruction)
                elif next_token.token_type == TokenType.VARIABLE_TYPE:
                    self.symbol_table.add_variable(token, next_token, tokens[i + 2])
            if token.token_type == TokenType.EOL:
                current_instruction += 1
        print(self.symbol_table.table, self.symbol_table.memory[:30])

    def tokenize_instructions(self, input_text: str) -> [[Token]]:
        self.tokens = []
        for line in input_text.splitlines():
            while self.current < len(line):
                if not self.is_whitespace(line[self.current]): 
                    token = self.next_token(line, len(line))
                    self.tokens.append(token)
                self.current += 1
            self.tokens.append(Token(TokenType.EOL, "\n"))
            self.current = 0
        return self.tokens

    def next_token(self, input_text: str, end: int) -> Token:
        start = self.current
        inside_string = False

        while self.current < end:
            if self.current + 1 < end and input_text[self.current + 1] == ',' and not inside_string:
                return Token(self.get_token_type(input_text[start:self.current + 1]), input_text[start:self.current + 1])

            elif not inside_string and self.current + 1 < end and self.is_whitespace(input_text[self.current + 1]):
                literal = input_text[start:self.current + 1]
                if len(literal) > 3 and literal[-2:] in condition_literals:
                    self.current -= 2
                    return Token(self.get_token_type(literal[:-2]), literal[:-2])
                if input_text[self.current + 1] == ":":
                    self.current += 1
                    return self.format_token(input_text[start:self.current + 1])
                return self.format_token(input_text[start:self.current + 1])

            elif not inside_string and input_text[self.current] == '"':
                inside_string = True
            elif inside_string and input_text[self.current] == '"':
                return self.format_token(input_text[start:self.current + 1])

            self.current += 1

            if self.current == end and end - start > 0:
                return self.format_token(input_text[start:self.current + 1])

        return Token(self.get_token_type(input_text[start:self.current]), input_text[start:self.current])

    def format_token(self, s: str) -> Token:
        token = Token()
        token.token_type = self.get_token_type(s)
        if token.token_type == TokenType.VARIABLE_NAME:
            token.literal = s[:-1]
        elif token.token_type == TokenType.VARIABLE_TYPE:
            token.literal = s[1:]
        elif token.token_type == TokenType.VARIABLE_REFERENCE:
            token.literal = s
        elif token.token_type == TokenType.STRING:
            token.literal = s[1:-1]
        else:
            token.literal = s

        return token

    def get_token_type(self, literal: str) -> TokenType:
        if literal == ',':
            return TokenType.COMMA

        if literal in mnemonic_literals:
            return TokenType.MNEMONIC
        
        if literal in condition_literals:
            return TokenType.CONDITION
        
        if self.symbol_table.check(literal):
            return TokenType.VARIABLE_REFERENCE
        
        if len(literal) > 1:
            if literal[0] == 'r' and self.is_digit(literal[1:]):
                return TokenType.REGISTER
            elif literal[0] == '#':
                return TokenType.CONSTANT
            elif literal[-1] == ':':
                return TokenType.VARIABLE_NAME
            elif literal[0] == '.':
                return TokenType.VARIABLE_TYPE
            elif self.is_digit(literal):
                return TokenType.NUMBER
            elif literal[0] == '"' and literal[-1] == '"':
                return TokenType.STRING
        return TokenType.ILLEGAL

