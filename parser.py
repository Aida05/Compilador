from ply import yacc
# importar lexico
import lexico
tokens = lexico.tokens

# diccionario de variables
variables = {}
precedence = (
    ('nonassoc', 'MAYORQUE', 'MENORQUE', 'MAYORIGUALQUE','MENORIGUALQUE','IGUAL','IGUALA','DIFERENTE','DISTINTO','IN','NOTIN','IS','ISNOT'),
    ('left','SUMA','RESTA'),
    ('left','MULTIPLICACION','DIVISION')   
    )

def p_asignacion(p):
    """sentencia : IDENTIFICADOR IGUAL expresion"""
    print("\t"+str(p[1])+" = "+str(p[3]))
    variables[p[1]] = p[3]
    print("-> Asignacion de variable")

def p_sentencia_expr(p):
    """sentencia : expresion
                | if_stc
                | expresionRelacional
                | expresionLogica
                |  print_stc
                | expresionGrupo"""
    if(p[1]!=None):
        print (p[1])

def p_expresion_logica(p):
    """expresionLogica : PARENIZQ expresiones OR expresiones PARENDER
                | PARENIZQ expresiones AND expresiones PARENDER 
                | NOT PARENIZQ expresiones PARENDER"""
    print ("Expresion logica")


def p_expresiones(p):
    """expresiones : expresionRelacional
                | expresion"""

def p_expresion_relacional(p):
    """expresionRelacional : expresion MAYORQUE terminal
                |  expresion MENORQUE terminal
                | expresion MAYORIGUALQUE terminal
                | expresion MENORIGUALQUE terminal
                | expresion IN terminal
                | expresion NOTIN terminal
                | expresion IS terminal
                | expresion ISNOT terminal
                | expresion DIFERENTE terminal
                | expresion DISTINTO terminal
                | expresion IGUAL terminal
                | expresion IGUALA terminal"""
    print ("Expresion de comparacion")

def p_expresion_aritmetica(p):
    """expresion : expresion SUMA terminal
                |  expresion RESTA terminal
                |  expresion MULTIPLICACION terminal
                |  expresion DIVISION terminal"""
    try:
        if p[2] == '+'  : p[0] = p[1] + p[3]
        elif p[2] == '-': p[0] = p[1] - p[3]
        elif p[2] == '*': p[0] = p[1] * p[3]
        elif p[2] == '/': p[0] = p[1] / p[3]
        print("-> Expresion aritmetica")
    except:
        print("Error aritmetico")

def p_parentesis(p):
    """expresionGrupo : PARENIZQ expresion PARENDER"""

def p_test(p):
    'test : PARENIZQ expresionRelacional PARENDER'

def p_if_stc(p):
    'if_stc : IF test PUNTOS'
    print("Linea IF correcta")

def p_print_stc(p):
    'print_stc : PRINT PARENIZQ STRING PARENDER'
    print("Linea PRINT correcta")

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
    print("Error en la sintaxis")

# constructor de la clase yacc
yacc.yacc()

print("\n\tANALIZADOR SINTACTICO DEL LENGUAJE PYTHON\n\tPara salir escribe 'salir'")
salir=True
while (salir):
    texto=raw_input("\n\tINGRESA UNA LINEA DE CODIGO PARA ANALIZAR:\n\t")
    if (texto=="salir"):
        salir=False
    else:
        yacc.parse(texto)
      
else:
    print("\n\tFIN DE EJECUCION\n")



# mostrar variables guardadas
#print(variables)
