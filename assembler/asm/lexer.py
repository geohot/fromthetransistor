import os
import enum 
import sys

MNEMONICS = ["mov"] # add, cmp, ...

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
        return self.token_type.__str__()

def tokenize(text: str) -> [Token]:
    lines = text.splitlines()
    tokens = []
    for line in lines:
        start = 0
        while start < len(line):
            (token, end) = get_next_token(line, start)
            start = end
            tokens.append(token)
        tokens.append(Token(TokenType.EOL, "\n"))

    return tokens
            
def get_next_token(s: str, start: int) -> (Token, int):
    if s[start] == ",":
        return (Token(TokenType.COMMA, s[start]), start + 1)
    for i in range(start, len(s)):
        if is_whitespace(s[i]) or s[i] == ",":
            literal = s[start:i] 
            if is_whitespace(s[i]):
                return (get_literal_token(literal), i + 1)
            return (get_literal_token(literal), i)

    return (get_literal_token(s[start:]), len(s))

def get_literal_token(literal: str) -> Token:
    token = Token(TokenType.ILLEGAL, literal)

    if literal in MNEMONICS:
        token.token_type = TokenType.MNEMONIC

    elif literal == ",":
        token.token_type = TokenType.COMMA

    elif len(literal) > 0:
        if literal[0] == 'r':
            token.token_type = TokenType.REGISTER

        elif literal[0] == '#':
            token.token_type = TokenType.CONSTANT

    return token

# FIX: add new lines, 
def is_whitespace(ch: str) -> bool:
    return ch == " "
