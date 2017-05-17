# Lexer for Simple1

from ply import *

reserved = {
    'get' : 'GET',
    'put' : 'PUT',
    'if' : 'IF',
    'else' : 'ELSE',
    'while' : 'WHILE'
}

literals = [':',';','+','-','*','/','(',')','{','}']
tokens = ['EQ', 'LE', 'INTEGER', 'ID'] + list(reserved.values())

t_EQ      = r'=='
t_LE      = r'<='
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_MULT    = r'\*'

t_ignore = ' \t'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

def t_INTEGER(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t

def t_COMMENT(t):
    r'//.*'
    pass

def t_NEWLINE(t):
    r'\n'
    pass

def t_error(t):
    print("Illegal character %s" % t.value[0])
    t.lexer.skip(1)

# build the lexer
lexer = lex.lex(debug=0)







       
   
  
            






