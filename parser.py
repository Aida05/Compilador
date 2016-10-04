from ply import yacc
# importar lexico
import lexico
tokens = lexico.tokens

# diccionario de variables
variables = {}
precedence = (
    ('nonassoc', 'MAYORQUE', 'MENORQUE', 'MAYORQUEIGUAL','MENORQUEIGUAL','IGUAL','COMPARACION','DIFERENTE','IN','IS'),
    ('left','SUMA','RESTA'),
    ('left','MULTIPLICACION','DIVISION')
)
def p_asignacion(p):
    """sentencia : IDENTIFICADOR IGUAL expresion"""
    print(str(p[1])+" = "+str(p[3]))
    variables[p[1]] = p[3]
    print("-> Asignacion de Variable")
def p_sentencia_expr(p):
    """sentencia : expresion
                | condicional
                | expresionRelacional
                |  print_stc
                | expresionGrupo
                | expresionLogica
                | for_stc
                | funcion"""
    if(p[1]!=None):
        print (p[1])
def p_expresion_logica(p):
    """expresionLogica : PARENIZQ expresion OR expresion PARENDER
                | PARENIZQ expresion AND expresion PARENDER
                | NOT PARENIZQ expresion PARENDER
                | expresion OR expresion
                | expresion AND expresion
                | NOT expresion"""
    print ("Expresion logica correcta")
def p_expresion_relacional(p):
    """expresionRelacional : expresion MAYORQUE terminal
                |  expresion MENORQUE terminal
                | expresion MAYORQUEIGUAL terminal
                | expresion MENORQUEIGUAL terminal
                | expresion DIFERENTE terminal
                | expresion COMPARACION terminal"""
    print ("Expresion comparacion correcta")

def p_expresion(p):
    """expresion : expresion SUMA terminal
                |  expresion RESTA terminal
                |  expresion MULTIPLICACION terminal
                |  expresion DIVISION terminal"""
    try:
        if p[2] == '+'  : p[0] = p[1] + p[3]
        elif p[2] == '-': p[0] = p[1] - p[3]
        elif p[2] == '*': p[0] = p[1] * p[3]
        elif p[2] == '/': p[0] = p[1] / p[3]
        print("-> Expresion aritmetica correcta")
    except:
        print("Error aritmetico")
def p_parentesis(p):
    "expresionGrupo : PARENIZQ expresion PARENDER"
    p[0] = p[2]
def p_test(p):
    """test : expresionRelacional
          | expresionLogica"""
def p_cond_stc(p):
    """condicional : IF test PUNTOS
              | ELIF test PUNTOS
              | ELSE PUNTOS
    """
    print("Linea condicional correcta")
def p_funtion(p):
    """funcion : DEF IDENTIFICADOR PARENIZQ PARENDER PUNTOS
                | DEF IDENTIFICADOR PARENIZQ IDENTIFICADOR PARENDER PUNTOS
                """
    print("Funcion definida")

def p_print_stc(p):
    'print_stc : PRINT PARENIZQ STRING PARENDER'
    print("Linea PRINT correcta")
def p_expresion_terminal(p):
    """expresion : terminal"""
    p[0] = p[1]
def p_for(p):
    """for_stc : FOR IDENTIFICADOR IN STRING PUNTOS
                | FOR IDENTIFICADOR IN IDENTIFICADOR PUNTOS"""
    print("Sentencia For correcta")
def p_terminal_numero(p):
    """terminal : NUMERO
                | STRING"""
    p[0] = p[1]
    return True

def p_terminal_variable(p):
    """terminal : IDENTIFICADOR"""
    try:
        p[0] = variables[p[1]]
    except LookupError:
        print("Valor no definido")

def p_error(p):
    #print("Error de sintaxis en token ")
    if(p):
        print("Error de sintaxis en token "+str(p.type))
    else:
        print("Error de sintaxis en token ")


# constructor de la clase yacc
yacc.yacc()

archivo=input("Codigo a verificar> \n")
codigo=open(archivo+".txt", "r")
for linea in codigo:
    _linea=linea.strip('\n')
    entrada = str(_linea)
    yacc.parse(entrada)


# mostrar variables guardadas
#print(variables)
