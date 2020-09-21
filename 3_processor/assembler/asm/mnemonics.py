from enum import Enum

class Mnemonic(Enum):
    MOVE = 'mov'
    ADD = 'add'
    AND = 'and'
    LOAD = 'ldr'
    COMPARE = 'cmp'
    STR = 'str'
    JUMP = 'jmp'
    OR = 'orr'
    XOR = 'xor'
    POP = 'pop'
    PUSH = 'push'
    JEQ = 'jeq'

mnemonic_literals = list(map(lambda c: c.value, Mnemonic))

