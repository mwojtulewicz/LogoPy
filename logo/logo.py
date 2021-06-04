# -------------------------------------------------------------
# logo.py
# 
# Logo iterpreter
#--------------------------------------------------------------


# Lexer

# reserved keywords
reserved = {
    'if': 'IF',
    'ifelse': 'IFELSE',
    'true': 'TRUE',
    'false': 'FALSE',
    'make': 'MAKE',
    'print': 'PRINT',
    'repeat': 'REPEAT',
    'repcount': 'REPCOUNT',
    'fd': 'FORWARD',
    'bk': 'BACK',
    'rt': 'RIGHT',
    'lt': 'LEFT',
    'pu': 'PENUP',
    'pd': 'PENDOWN',
    'st': 'SHOW',
    'ht': 'HIDE',
    'setx': 'SETX',
    'sety': 'SETY',
    'seth': 'SETH',
    'setxy': 'SETXY',
    'setpencolor': 'SETPC',
    'setbgcolor': 'SETBC',
    'setpensize': 'SETPS',
    'home': 'HOME',
    'speed': 'SPEED',
    'clean': 'CLEAN',
    'reset': 'RESET',
    'random': 'RANDOM'
}

# tokens keywords
tokens = [
    'STRING', 'FLOAT', 'INT',
    'LBR', 'RBR', 'LPAR', 'RPAR', 
    'QUOTE', 'COLON', 'COMMA',
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
t_COMMA  = r','
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
    ('right', 'RANDOM'),
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
              | ifelse_statement
              | variable_declaration
              | print_statement
    '''
    p[0] = [p[1]]

def p_turtle_instruction(p):
    '''
    turtle_instruction : SETXY LBR expression COMMA expression RBR
                       | FORWARD expression
                       | BACK expression
                       | RIGHT expression
                       | LEFT expression
                       | SETX expression
                       | SETY expression
                       | SETH expression
                       | SPEED expression
                       | SETPS expression
                       | SETPC word
                       | SETBC word
                       | PENUP
                       | PENDOWN
                       | SHOW
                       | HIDE
                       | HOME
                       | CLEAN
                       | RESET
    '''
    if len(p)==7:
        p[0] = (p[1], p[3], p[5])
    elif len(p)==3:
        p[0] = (p[1], p[2])
    else:
        p[0] = (p[1], None)

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

def p_ifelse_statement(p):
    '''
    ifelse_statement : IFELSE condition LBR statement_list RBR LBR statement_list RBR
    '''
    p[0] = (p[1], p[2], p[4], p[7])

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
               | REPCOUNT
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
        p[0] = ('uminus', p[2])
    else:
        p[0] = (-1) * p[2]

def p_expression_random(p):
    '''
    expression : RANDOM expression
    '''
    p[0] = (p[1], p[2])

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
    return f"Syntax error at {p.value!r}"


# ----------------------------------------------------------------------
# Interpreter

import turtle
import random

turtle.title('LogoPy')
turtle.shape("turtle")
turtle.mode('logo')
turtle.speed(0)

# scope
env = { }
env['repcount'] = 0

def run(program):
    for statement in program:
        execute(statement)

def execute(s):
    global env
    fun = s[0]
    arg1 = s[1]
    arg2 = s[2] if len(s)>2 else None
    arg3 = s[3] if len(s)>3 else None
    # turtle instruction
    if fun == 'setxy':
        turtle.setposition(calc(arg1), calc(arg2))
    elif fun == 'fd':
        turtle.forward(calc(arg1))
    elif fun == 'bk':
        turtle.back(calc(arg1))
    elif fun == 'rt':
        turtle.right(calc(arg1))
    elif fun == 'lt':
        turtle.left(calc(arg1))
    elif fun == 'setx':
        turtle.setx(calc(arg1))
    elif fun == 'sety':
        turtle.sety(calc(arg1))
    elif fun == 'seth':
        turtle.setheading(calc(arg1))
    elif fun == 'setpensize':
        turtle.pensize(calc(arg1))
    elif fun == 'setpencolor':
        turtle.pencolor(arg1)
    elif fun == 'setbgcolor':
        turtle.pencolor(arg1)
    elif fun == 'speed':
        turtle.speed(calc(arg1))
    elif fun == 'pu':
        turtle.penup()
    elif fun == 'pd':
        turtle.pendown()
    elif fun == 'st':
        turtle.showturtle()
    elif fun == 'ht':
        turtle.hideturtle()
    elif fun == 'home':
        turtle.home()
    elif fun == 'clean':
        turtle.clear()
    elif fun == 'reset':
        turtle.reset()
    # repeat
    elif fun == 'repeat':
        for i in range(0, int(calc(arg1))):
            env['repcount'] = i+1
            run(arg2)
    # if
    elif fun == 'if':
        if eval(arg1):
            run(arg2)
    elif fun == 'ifelse':
        if eval(arg1):
            run(arg2)
        else:
            run(arg3)
    # variable declaration
    elif fun == 'make':
        env[arg1] = calc(arg2)
    # print
    elif fun == 'print_word':
        print(arg1)
    elif fun == 'print_expr':
        print(calc(arg1))

def calc(e):
    global env
    if type(e) == tuple:
        id = e[0]
        arg1 = e[1]
        arg2 = e[2] if len(e)>2 else None
        if id == '+':
            return calc(arg1) + calc(arg2)
        elif id == '-':
            return calc(arg1) - calc(arg2)
        elif id == '*':
            return calc(arg1) * calc(arg2)
        elif id == '/':
            return calc(arg1) / calc(arg2)
        elif id == '^':
            return calc(arg1) ** calc(arg2)
        elif id == 'var':
            try:
                return env[arg1]
            except LookupError:
                print(f"Undefined variable {arg1}")
                return
        elif id == 'uminus':
            return (-1) * calc(arg1)
        elif id == 'random':
            return random.randrange(calc(arg1))
    else:
        return e

def eval(c):
    global env
    if type(c) != tuple:
        return c
    else:
        op = c[0]
        arg1 = calc(c[1])
        arg2 = calc(c[2])
        if op == '>':
            return arg1 > arg2
        elif op == '<':
            return arg1 < arg2
        elif op == '>=':
            return arg1 >= arg2
        elif op == '<=':
            return arg1 <= arg2
        elif op == '=':
            return arg1 < arg2
        elif op == '!=':
            return arg1 != arg2

# ----------------------------------------------------------------------
# main


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

    # excecute
    print('\nOutput :')
    if p is None:
        print("Syntax error")
    else:
        run(p)

print('\n')
turtle.bye()
