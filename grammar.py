# reserved keywoards
# tokens keywoards

reserved = {
    'if': 'IF',
    'true': 'TRUE',
    'false': 'FALSE',
    'make': 'MAKE',
    'print': 'PRINT',
    'repeat': 'REPEAT',
    'fd': 'FORWARD',
    'bk': 'BACK',
    'rt': 'RIGHT',
    'lt': 'LEFT',
    'pu': 'PENUP',
    'pd': 'PENDOWN'
}

tokens = [
    'STRING', 'FLOAT', 'INT',
    'LBR', 'RBR', 'LPAR', 'RPAR', 
    'QUOTE', 'COLON',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EQUALS',
    'GTE', 'LTE', 'GT', 'LT'
] + list(reserved.values())


# Tokens

t_LBR    = r'\['
t_RBR    = r'\]'
t_LPAR   = r'\('
t_RPAR   = r'\)'
t_QUOTE  = r'"'
t_COLON  = r':'
t_PLUS   = r'\+'
t_MINUS  = r'-'
t_TIMES  = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_GTE    = r'>='
t_LTE    = r'<='
t_GT     = r'>'
t_LT     = r'<'

def t_STRING(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value,'STRING')
    return t

def t_FLOAT(t):
    r'[+-]?\d*\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'[+-]?\d+'
    t.value = int(t.value)
    return t

# Ignored characters
t_ignore = " \t"

def t_error(t):
    print(f"Illegal character {t.value[0]!r}")
    t.lexer.skip(1)

# Build the lexer
import ply.lex as lex
lexer = lex.lex()


# testing
while True:
    try:
        s = input('logo > ')
    except EOFError:
        break
    
    lexer.input(s)
    
    while True:
        tok = lexer.token()
        if not tok:
            print()
            break
        print(tok)
