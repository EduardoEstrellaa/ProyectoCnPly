import statistics
import numpy as np
import math
import ply.yacc as yacc
from AnalizadorLexico import tokens
variable_Lista = {}

def p_expression_CONJUNTO(p):
    '''
    expression : PR_POBLACION PUNTO PR_DISCRETA VARIABLE CORCHETE_DER set_elements CORCHETE_IZQ
               | PR_MUESTRA PUNTO PR_CONTINUA VARIABLE CORCHETE_DER set_elements CORCHETE_IZQ
               | PR_POBLACION PUNTO PR_CONTINUA VARIABLE CORCHETE_DER set_elements CORCHETE_IZQ
               | PR_MUESTRA PUNTO PR_DISCRETA VARIABLE CORCHETE_DER set_elements CORCHETE_IZQ
    '''
    variable = p[4]
    conjunto = p[6]
    variable_Lista[variable] = conjunto
    p[0] = conjunto

def p_expression_MODA(p):
    'expression : Calc_MODA PARENTESIS_DER VARIABLE PARENTESIS_IZQ'
    variable = p[3]
    
    # Verificar si la variable existe en la Lista
    if variable in variable_Lista:
        data = variable_Lista[variable]
        moda = statistics.mode(data)
        p[0] = moda
    else:
        # Si no existe en la Lista, envia un mensaje
        print(f"Error: La variable {variable} no ha sido asignada.")

def p_expression_MEDIANA(p):
    'expression : Calc_MEDIANA PARENTESIS_DER VARIABLE PARENTESIS_IZQ'
    variable = p[3]

    if variable in variable_Lista:
        data = variable_Lista[variable]
        mediana = statistics.median(data) 
        p[0] = mediana
    else:
        print(f"Error: La variable {variable} no ha sido asignada.")

def p_expression_PROMEDIO(p):
    'expression : Calc_MEDIA_ARITMETICA PARENTESIS_DER VARIABLE PARENTESIS_IZQ'
    variable = p[3]

    if variable in variable_Lista:
        data = variable_Lista[variable]
        promedio = statistics.mean(data) 
        p[0] = promedio
    else:
         print(f"Error: La variable {variable} no ha sido asignada.")

def p_expression_DesvESTANDAR(p):
    'expression : Calc_DESV_ESTANDAR PARENTESIS_DER VARIABLE PARENTESIS_IZQ'
    variable = p[3]
    if variable in variable_Lista:
        data = variable_Lista[variable]
        dv = statistics.pstdev(data) 
        p[0] = dv
    else:
         print(f"Error: La variable {variable} no ha sido asignada.")

def p_expression_Calc_VARIANZA(p):
    'expression : Calc_VARIANZA PARENTESIS_DER VARIABLE PARENTESIS_IZQ'
    variable = p[3]
    if variable in variable_Lista:
        data = variable_Lista[variable]
        varianza = statistics.pvariance(data) 
        p[0] = varianza
    else:
         print(f"Error: La variable {variable} no ha sido asignada.")


def p_expression_ADICION(p):
    'expression : ADICION expression COMA term'
    p[0] = p[2] + p[4]

def p_expression_SUSTRACCION(p):
    'expression : SUSTRACCION expression COMA term'
    p[0] = p[2] - p[4]

def p_expression_PRODUCTO(p):
    'expression : PRODUCTO expression COMA term'
    p[0] = p[2] * p[4]

def p_expression_IMPRIME(p):
    'expression : IMPRIME_DATOS PARENTESIS_DER expression PARENTESIS_IZQ'
    dato = p[3]
    if dato in variable_Lista:
        dt = variable_Lista[dato]
        p[0] = dt
    else:
        p[0] = p[3]

def p_expression_POTENCIA(p):
    'expression : expression POTENCIA term'
    p[0] = p[1] ** p[3]

def p_expression_RAIZ(p):
    'expression : expression RAIZ'
    p[0] = math.sqrt(p[1]) 

def p_expression_LOGICA(p):
    '''
    expression : expression OP_MENOR expression
                | expression OP_MAYOR expression
    '''
    if p[2] == "<:" : p[0] = p[1] < p[3]
    elif p[2] == ":>" : p[0] = p[1] > p[3] 

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUMEROS'
    p[0] = p[1]

def p_st_variable(p):
    'expression : VARIABLE'
    p[0] = p[1]

def p_set_elements_single(p):
    '''
    set_elements : expression
    '''
    p[0] = [p[1]]

def p_set_elements_multiple(p):
    '''
    set_elements : expression COMA set_elements
    '''
    p[0] = [p[1]] + p[3]

def p_expression_number(p):
    '''
    expression : NUMEROS
    '''
    p[0] = p[1]

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()
while True:
    try:
        print('\033[92m+------------------------------------------------+')
        s = input('| Analizador Sintactico                          |\n+------------------------------------------------+\n\033[0m')
    except EOFError:
        break
    if not s:
        continue
    result = parser.parse(s)
    print('\033[96m+-----------------------------------------------------+')
    print('|                    Resultado                        |')
    print('+-----------------------------------------------------+')
    print(f'|   Entrada : {s.ljust(39)} |')
    print('|                                                     |')
    print(f'|   Salida  : {str(result).ljust(39)} |')
    print('+-----------------------------------------------------+\n\033[0m')


