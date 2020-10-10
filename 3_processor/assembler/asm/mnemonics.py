from enum import Enum
# A8.3 Conditional execution
class Mnemonic(Enum):
    MOVE = 'mov'
    ADD = 'add'
    AND = 'and'
    LOAD = 'ldr'
    COMPARE = 'cmp'
    STR = 'str'
    B = 'b'
    OR = 'orr'
    XOR = 'xor'
    POP = 'pop'
    PUSH = 'push'

mnemonic_literals = list(map(lambda c: c.value, Mnemonic))

