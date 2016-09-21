import ply.lex as lex


tokens = [ 'NAME','NUMBER','PLUS','MINUS','TIMES','DIVIDE', 'EQUALS' ]
t_ignore= ' \t'
t_PLUS= r'\+'
t_MINUS=r'\-'
t_TIMES=r'\*'
t_DIVIDE=r'/'
t_EQUALS=r'='
t_NAME   = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
lex.lex()
lex.input("x = 3 * 4 + 5 * 6")
while True:
    tok = lex.token()
    if not tok:
        break
    else:
        print(tok.type)
        #tok.type tipo de token
        #tok.value valor del token
        #tok.line lugar del token
        #tok.lexpos
