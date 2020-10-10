from enum import Enum

class Condition(Enum):
    EQ = 'eq'
    NE = 'ne'
    GT = 'gt'
    LT = 'lt'
    HS = 'hs'
    LO = 'lo'
    MI = 'mi'
    PL = 'pl'
    AL = 'al'
    NV = 'nv'
    VS = 'vs'
    VC = 'vc'
    HI = 'hi'
    LS = 'ls'

condition_literals = list(map(lambda c: c.value, Condition))

condition_map = {
    'eq': '0000',
    'ne': '0001',
    'cs': '0010',
    'cc': '0011',
    'mi': '0100',
    'pl': '0101',
    'vs': '0110',
    'vc': '0111',
    'hi': '1000',
    'ls': '1001',
    'ge': '1010',
    'lt': '1011',
    'gt': '1100',
    'le': '1101',
    'no': '1110', # none
}