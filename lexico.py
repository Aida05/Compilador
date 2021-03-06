import ply.lex as lex
#Diccionario de palabras reservadas
reservada = {
   'if' : 'IF',
   'then' : 'THEN',
   'else' : 'ELSE',
   'for': 'FOR',
   'while' : 'WHILE',
   'assert':'ASSERT',
   'and': 'AND',
   'break': 'BREAK',
   'class': 'CLASS',
   'continue': 'CONTINUE',
   'def': 'DEF',
   'del': 'DEL',
   'elif': 'ELIF',
   'except': 'EXCEPT',
   'exec': 'EXEC',
   'finally': 'FINALLY',
   'for': 'FOR',
   'from': 'FROM',
   'global': 'GLOBAL',
   'or': 'OR',
   'not': 'NOT',
   'import': 'IMPORT',
   'in': 'IN',
   'is': 'IS',
   'lambda': 'LAMBDA',
   'pass': 'PASS',
   'print': 'PRINT',
   'raise': 'RAISE',
   'return': 'RETURN',
   'try': 'TRY',
}


tokens = ['PARENIZQ','PARENDER','PUNTOS','STRING','MAYORQUEIGUAL', 'MENORQUEIGUAL','MAYORQUE','MENORQUE', 'DIFERENTE', 'COMPARACION','HEX','IDENTIFICADOR','NUMERO','SUMA','RESTA','MULTIPLICACION','DIVISION', 'IGUAL', ]+ list(reservada.values())
t_HEX=r'0x[0-9aA-fF]+'
t_ignore= ' \t'
t_SUMA= r'\+'
t_RESTA=r'\-'
t_MULTIPLICACION=r'\*'
t_DIVISION=r'/'
t_IGUAL=r'='
t_MAYORQUE=r'>'
t_MENORQUE=r'<'
t_MAYORQUEIGUAL=r'>='
t_MENORQUEIGUAL=r'=<'
t_DIFERENTE=r'!='
t_COMPARACION=r'=='
t_PUNTOS=r':'
t_PARENIZQ=r'\('
t_PARENDER=r'\)'
def t_STRING(t):
    r"'([^\\']+|\\'|\\\\)*'"
    t.value=str(t.value)
    return t
def t_IDENTIFICADOR(t):
    r"[aA-zZ_]+[0-9_aA-zZ]*"
    t.type = reservada.get(t.value,'IDENTIFICADOR')
    return t
def t_NUMERO(t):
    r"""(\d+(\.\d*)?|\.\d+)([eE][-+]? \d+)?"""
    t.value = float(t.value)
    return t
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
def t_comment(t):
    r"[ ]*\043[^\n]*"  # \043 is '#'
    pass
lex.lex()
lex.input("if:( )")

"""while True:
    tok = lex.token()
    if not tok:
        break
    else:
        print(tok.type)
        #tok.type
        #tok.value
        #tok.line
        #tok.lexpos"""
