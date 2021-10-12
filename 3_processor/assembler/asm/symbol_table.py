from lexer import Token, TokenType, Lexer

MAX_ENTRIES = 1024 # Maximum number of entries in this Symbol Table
MAX_LENGTH = 20 # Maximum length of any symbol or variable name

def num_to_bin(num: int, bit_count: int) -> str:
    s = bin(num)[2:]
    for _ in range(bit_count - len(s)):
        s = '0' + s
    return s

def bin_to_bin(bin: str, bit_count: int) -> str:
    for _ in range(bit_cound - len(s)):
        s = '0' + s
    return s

def ascii_to_bin(str: str, bit_count: int) -> str:
    pass
    

class SymbolEntry:
    def __init__(self, address):
        self.address = address

class SymbolTable:
    def __init__(self):
        self.memory_counter = 15
        self.table = {}
        self.memory = [None for i in range(0, MAX_ENTRIES)]

    def add_label(self, label: str, current_instruction: int) -> None:
        self.table[label] = self.memory_counter
        self.memory[self.memory_counter] = current_instruction + 1
        self.memory_counter += 1
    
    def add_variable(self, declaration: Token, type: Token, value: Token) -> None:
        self.table[declaration.literal] = self.memory_counter
        self.memory[self.memory_counter] = value.literal
        self.memory_counter += 1

    def check(self, variable_name: str) -> bool:
        return variable_name in self.table
             
    def read(self, variable_name: str) -> str:
        if variable_name in self.table:
            return self.memory[self.table[variable_name]]
        return Exception(f'Reference error, symbol {variable_name} not defined')