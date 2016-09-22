from ply import yacc
# importar lexico
import lexico
tokens = lexico.tokens

def p_asignacion(p):
    """asignacion : NAME EQUALS expresion"""
    p[0] = p[3]
    print("-> ASIGNACIÓN")
    #print("\t"+str(p[0])+" = "+str(p[3]))

def p_expresion(p):
    """expresion : expresion PLUS terminal
                |  expresion MINUS terminal
                |  expresion TIMES terminal
                |  expresion DIVIDE terminal
                |  terminal"""
    print("-> EXPRESIÓN")

def p_terminal(p):
    """terminal : NUMBER
                | NAME"""
    print("-> TERMINAL")

def p_error(p):
    print("Syntax error")

# constructor de la clase yacc
yacc.yacc()
entrada1 = "x = 20"
entrada2 = "x = x + 5"
yacc.parse(entrada1)
print("\tbreak")
yacc.parse(entrada2)
