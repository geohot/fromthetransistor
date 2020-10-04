SYMBOL_TABLE_MEM_OFFSET = 1024

class SymbolTable:
    def __init__(self):
        self.mem_counter = SYMBOL_TABLE_MEM_OFFSET 
        self.symbol_memory_address = {}
    
    def assign_memory_address(self, variable_name: str):
        if variable_name not in self.symbol_memory_address:
            self.symbol_memory_address[variable_name] = self.mem_counter
            self.mem_counter += 1
             
    def read(self, variable_name: str) -> str:
        if not variable_name in self.symbol_memory_address:
            return Exception(f'Reference error, symbol {variable_name} not defined')
        return self.symbol_memory_address[variable_name]
