from lexer import Lexer, Token, TokenType

asm_source_code = '''
    mov r0, #10
    mov r1, r0
    num: .short 010
    msg: .string "Hello, arm"
    addlt r0, r0, #1
'''

want_tokens = [
    Token(token_type=TokenType.EOL, literal= '\n'),

    Token(token_type=TokenType.MNEMONIC, literal= 'mov'),
    Token(token_type=TokenType.REGISTER, literal= 'r0'),
    Token(token_type=TokenType.COMMA, literal= ','),
    Token(token_type=TokenType.CONSTANT, literal= '#10'),
    Token(token_type=TokenType.EOL, literal= '\n'),

    Token(token_type=TokenType.MNEMONIC, literal= 'mov'),
    Token(token_type=TokenType.REGISTER, literal= 'r1'),
    Token(token_type=TokenType.COMMA, literal= ','),
    Token(token_type=TokenType.REGISTER, literal= 'r0'),
    Token(token_type=TokenType.EOL, literal= '\n'),

    Token(token_type=TokenType.VARIABLE_NAME, literal= 'num'),
    Token(token_type=TokenType.VARIABLE_TYPE, literal= 'short'),
    Token(token_type=TokenType.NUMBER, literal= '010'),
    Token(token_type=TokenType.EOL, literal= '\n'),

    Token(token_type=TokenType.VARIABLE_NAME, literal= 'msg'),
    Token(token_type=TokenType.VARIABLE_TYPE, literal= 'string'),
    Token(token_type=TokenType.STRING, literal= 'Hello, arm'),
    Token(token_type=TokenType.EOL, literal= '\n'),

    Token(token_type=TokenType.MNEMONIC, literal= "add"),
    Token(token_type=TokenType.CONDITION, literal= "lt"),
    Token(token_type=TokenType.REGISTER, literal= "r0"),
    Token(token_type=TokenType.COMMA, literal= ","),
    Token(token_type=TokenType.REGISTER, literal= "r0"),
    Token(token_type=TokenType.COMMA, literal= ","),
    Token(token_type=TokenType.CONSTANT, literal= "#1"),
    Token(token_type=TokenType.EOL, literal= "\n"),
]

def test():
    lexer = Lexer()

    tokens = lexer.tokenize_instructions(asm_source_code)

    print("Testing the coins...")
    '''
    if len(tokens) != len(want_tokens):
        print(f'have {len(tokens)}, want {len(want_tokens)}')
        exit()
    '''
    for i in range(len(tokens)):
        if tokens[i].token_type != want_tokens[i].token_type:
            print(f'Have token {tokens[i]}, want {want_tokens[i]}')
            exit()
        if str(tokens[i].literal) != str(want_tokens[i].literal):
            print(f'Have token literal `{tokens[i].literal}`, want `{want_tokens[i].literal}`')
            exit()
    
    print("Good coins :3 Tests Passed!")

test()
