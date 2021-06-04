# -------------------------------------------------------------
# logo.py
# 
# Logo iterpreter
#--------------------------------------------------------------


# Lexer

# reserved keywords
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

# tokens keywords
tokens = [
    'STRING', 'FLOAT', 'INT',
    'LBR', 'RBR', 'LPAR', 'RPAR', 
    'QUOTE', 'COLON',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'POWER', 'EQUALS',
    'GTE', 'LTE', 'GT', 'LT', 'NE'
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
t_POWER  = r'\^'
t_EQUALS = r'='
t_GTE    = r'>='
t_LTE    = r'<='
t_GT     = r'>'
t_LT     = r'<'
t_NE     = r'!='

def t_STRING(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value,'STRING')
    return t

def t_FLOAT(t):
    r'\d*\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignored characters
t_ignore = " \t"

def t_error(t):
    print(f"Illegal character {t.value[0]!r}")
    t.lexer.skip(1)


# -----------------------------------------------------------------------
# Parser

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'POWER'),
    ('right', 'UMINUS')
)

def p_statement_list(p):
    '''
    statement_list : statement_list statement
                   | statement
    '''
    if len(p)==3:
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]


def p_statement(p):
    '''
    statement : turtle_instruction
              | repeat_statement
              | if_statement
              | variable_declaration
              | print_statement
    '''
    p[0] = [p[1]]

def p_turtle_instruction(p):
    '''
    turtle_instruction : FORWARD expression
                       | BACK expression
                       | RIGHT expression
                       | LEFT expression
                       | PENUP
                       | PENDOWN
    '''
    if len(p)==3:
        p[0] = (p[1], p[2])
    else:
        p[0] = (p[1])

def p_repeat_statement(p):
    '''
    repeat_statement : REPEAT expression LBR statement_list RBR 
    '''
    p[0] = (p[1], p[2], p[4])

def p_if_statement(p):
    '''
    if_statement : IF condition LBR statement_list RBR
    '''
    p[0] = (p[1], p[2], p[4])

def p_variable_declaration(p):
    '''
    variable_declaration : MAKE word expression
    '''
    p[0] = (p[1], p[2], p[3])

def p_print_statement_word(p):
    '''
    print_statement : PRINT word
    '''
    p[0] = ('print_word', p[2])

def p_print_statement_expression(p):
    '''
    print_statement : PRINT expression
    '''
    p[0] = ('print_expr', p[2])

def p_expression_int_float(p):
    '''
    expression : INT
               | FLOAT
    '''
    p[0] = p[1]

def p_expression_var(p):
    '''
    expression : name
    '''
    p[0] = ('var', p[1])

def p_expression_group(p):
    '''
    expression : LPAR expression RPAR
    '''
    p[0] = p[2]

def p_expression_uminus(p):
    '''
    expression : MINUS expression %prec UMINUS
    '''
    if type(p[2]) is tuple:
        p[0] = ('UMINUS', p[2])
    else:
        p[0] = -p[2]

def p_expression(p):
    '''
    expression : expression TIMES expression
               | expression DIVIDE expression
               | expression PLUS expression
               | expression MINUS expression
               | expression POWER expression
    '''
    p[0] = (p[2], p[1], p[3])

def p_condition_true_false(p):
    '''
    condition : TRUE
              | FALSE
    '''
    value = p[1]=='true'
    p[0] = value

def p_condition(p):
    '''
    condition : expression GT expression
              | expression LT expression
              | expression GTE expression
              | expression LTE expression
              | expression EQUALS expression
              | expression NE expression
    '''
    p[0] = (p[2], p[1], p[3])

def p_word(p):
    '''
    word : QUOTE STRING
    '''
    p[0] = p[2]

def p_name(p):
    '''
    name : COLON STRING
    '''
    p[0] = p[2]

def p_error(p):
    print(f"Syntax error at {p.value!r}")


# ----------------------------------------------------------------------
# using


# build the lexer
import ply.lex as lex
lexer = lex.lex()

# build the parser
import ply.yacc as yacc
parser = yacc.yacc()

# main loop
while True:
    try:
        s = input('\nlogo > ')
    except EOFError:
        break
    
    # lexer
    lexer.input(s)
    print('\ntokens : ',[(tok.type, tok.value) for tok in lexer])
    
    # parser
    p = parser.parse(s, lexer=lexer)
    print('\nAST    : ', p)