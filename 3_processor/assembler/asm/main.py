from lexer import *
from parser import *
# TODO: abstract out getting file text
def main():
    if len(sys.argv) < 2:
        print("should specify asm filename. example: python3 main.py asm.a")
        exit()

    filename = sys.argv[1]
    if len(filename) == 0:
        print("should specify asm filename. example: python3 main.py asm.a")
        exit()

    path = os.path.join(os.getcwd(), filename)
    asm_file = open(path, 'r')
    file_text = asm_file.read()

    instructions = tokenize_instructions(file_text) # [[mov, r1, #7], ...]
    print("look at my coins")
    for tokens in instructions:
        for token in tokens: 
            print(token)

    binary_instructions = []
    for instruction in instructions:
        binary_instruction = parse_instruction(instruction) # 32-bit binary number
        binary_instructions.append(binary_instruction)

    print("look at my binaries")

    # FIX: write all bin_instructions into a file
    for bin_inst in binary_instructions:
        print(bin_inst)
        
if __name__ == "__main__":
    main()
