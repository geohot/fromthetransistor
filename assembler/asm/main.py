from lexer import *

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

    tokens = tokenize(file_text)
    print("look at my coins")
    for token in tokens:
        print(token)
     
if __name__ == "__main__":
    main()
