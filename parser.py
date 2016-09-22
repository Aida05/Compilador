from ply import yacc
# importar lexico
import lexico
tokens = lexico.tokens

# diccionario de variables
variables = {}
precedence = (
    ('left','SUMA','RESTA'),
    ('left','MULTIPLICACION','DIVISION')
    )
def p_asignacion(p):
    """asignacion : IDENTIFICADOR IGUAL expresion"""
    print("\t"+str(p[1])+" = "+str(p[3]))
    variables[p[1]] = p[3]
    print("-> ASIGNACIÓN")

def p_expresion(p):
    """expresion : expresion SUMA terminal
                |  expresion RESTA terminal
                |  expresion MULTIPLICACION terminal
                |  expresion DIVISION terminal"""
    if p[2] == '+'  : p[0] = p[1] + p[3]
    elif p[2] == '-': p[0] = p[1] - p[3]
    elif p[2] == '*': p[0] = p[1] * p[3]
    elif p[2] == '/': p[0] = p[1] / p[3]
    print("-> EXPRESIÓN")

def p_expresion_terminal(p):
    """expresion : terminal"""
    p[0] = p[1]

def p_terminal_numero(p):
    """terminal : NUMERO"""
    p[0] = p[1]

def p_terminal_variable(p):
    """terminal : IDENTIFICADOR"""
    try:
        p[0] = variables[p[1]]
    except LookupError:
        print("Valor no definido")

def p_error(p):
    print("error")

# constructor de la clase yacc
yacc.yacc()

entrada = "x = 8 + 2 * 20"
yacc.parse(entrada)

# mostrar variables guardadas
print(variables)
