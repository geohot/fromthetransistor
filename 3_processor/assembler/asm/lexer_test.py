from lexer import *

asm_source_code = '''
   mov r0, #10
   mov r1, r0
'''

correct_tokens = [
    "token_type: EOL, literal: \n",
    "token_type: MNEMONIC, literal: mov",
    "token_type: REGISTER, literal: r0",
    "token_type: COMMA, literal: ,",
    "token_type: CONSTANT, literal: #10",
    "token_type: EOL, literal: \n",
    "token_type: MNEMONIC, literal: mov",
    "token_type: REGISTER, literal: r1",
    "token_type: COMMA, literal: ,",
    "token_type: REGISTER, literal: r0",
    "token_type: EOL, literal: \n"
]

def test():
    lexer = Lexer()

    tokens = lexer.tokenize_instructions(asm_source_code)

    print("Testing the coins...")

    if len(tokens) != len(correct_tokens):
        print(f'have {len(tokens)}, want {len(correct_tokens)}')
        exit()

    for i in range(len(tokens)):
        if tokens[i].__str__() != correct_tokens[i]:
            print(f'Have {tokens[i].__str__()}, want {correct_tokens[i]}')
            exit()
    
    print("Good coins :3 Tests Passed!")

test()
