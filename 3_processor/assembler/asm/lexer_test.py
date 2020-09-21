from lexer import *

asm_source_code = '''
mov r0, #10
mov r1, r0
'''

want_token_types = [
    [
        TokenType.EOL,
    ],
    [
        TokenType.MNEMONIC,
        TokenType.REGISTER,
        TokenType.COMMA,
        TokenType.ILLEGAL,
        TokenType.CONSTANT,
        TokenType.EOL,
    ],
    [
        TokenType.MNEMONIC,
        TokenType.REGISTER,
        TokenType.COMMA,
        TokenType.ILLEGAL,
        TokenType.REGISTER,
        TokenType.EOL,
    ],
]

def test():
    lines_tokens = tokenize_instructions(asm_source_code)
    print("testing the coins")
    if len(lines_tokens) != len(want_token_types):
        print(f'have {len(tokens)}, want {len(want_token_types)}')
        exit()
    for i in range(len(lines_tokens)):
        tokens = lines_tokens[i]
        for j in range(len(tokens)):
            if tokens[j].token_type != want_token_types[i][j]:
                print(f'line {i+1}: have {tokens[i]}, want {want_token_types[i][j]}')
                exit()

    print("good coins")

test()
