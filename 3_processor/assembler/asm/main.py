import sys
import os

from assembler import Assembler
from lexer import Lexer

def main():
    file_text = get_file_text()
    assembler = Assembler()
    lexer = Lexer()

    tokens = lexer.tokenize_instructions(file_text) # [[mov, r1, #7], ...]

    print("look at my coins")
    for token in tokens:
        print(token.__str__())

    bin_instructions = assembler.assemble_instructions(tokens)

    print("look at my binaries")
    # FIX: write all bin_instructions into a file
    for bin_inst in bin_instructions:
        print(bin_inst)
        
def get_file_text():
    if len(sys.argv) < 2:
        print("should specify asm filename. example: python3 main.py asm.a")
        exit()

    filename = sys.argv[1]
    if len(filename) == 0:
        print("should specify asm filename. example: python3 main.py asm.a")
        exit()

    path = os.path.join(os.getcwd(), f'3_processor/assembler/asm/{filename}')
    asm_file = open(path, 'r')
    file_text = asm_file.read()

    return file_text

if __name__ == "__main__":
    main()
