class Symbol_Table:
    def __init__(self):
        self.symbols = {}
    
    def store(self, literal: str, value: str) -> None:
        self.symbols[literal] = value
    
    def read(self, literal: str) -> str:
        if not literal in self.symbols:
            return Exception(f'Reference error, symbol {literal} not defined')
        return self.symbols[literal]