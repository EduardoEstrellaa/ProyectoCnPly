import sys
import ply.lex as lex

tokens = (

    # LISTA DE PALABRAS RESERVADAS
    # PR es Palabra Reservada xd
    'PR_MUESTRA','PR_POBLACION','PR_CONTINUA','PR_DISCRETA','PR_MEZCLA','PR_PROCEDIMIENTO',
    'PR_FIN_PROCEDIMIENTO',"PR_MED_TEN_CENTRAL",'PR_MED_DISPERSION','PR_INDIVIDUO',
    'PR_DEVUELVE',

    # LISTA DE SIMBOLOS Y OPERADORES 
    'RAIZ','ADICION','POTENCIA','DIVISION','PRODUCTO','SUSTRACCION',
    'SUMATORIA','IGUAL','OP_MENOR','OP_MAYOR','OP_IGUALDAD',
    'PARENTESIS_DER','PARENTESIS_IZQ','CORCHETE_DER','CORCHETE_IZQ',
    'PUNTO','COMA','IGUAL_FUNC',

    #FUNCIONES 
    'Calc_MEDIA_ARITMETICA','Calc_MEDIANA','Calc_MODA','Calc_DESV_ESTANDAR',
    'Calc_VARIANZA','ORDENA','AGREGA','IMPRIME_DATOS',

    # OTROS
    'COMENTARIOS','NUMEROS','VARIABLE',
)


# Caracteres Ignorados
t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("\t ERROR: Caracter Ilegal")
    print("\t\tLine: " + str(t.lexer.lineno) + "\t=> " + t.value[0])
    t.lexer.skip(1)



#Lista de Palabras reservadas

def t_PR_MUESTRA(t):
    r'MUESTRA'
    return t

def t_PR_POBLACION(t):
    r'POBLACION'
    return t

def t_PR_CONTINUA(t):
    r'CONTINUA'
    return t

def t_PR_DISCRETA(t):
    r'DISCRETA'
    return t

def t_PR_MEZCLA(t):
    r'MEZCLA'
    return t

def t_PR_PROCEDIMIENTO(t):
    r'PROCEDIMIENTO'
    return t

def t_PR_FIN_PROCEDIMIENTO(t):
    r'FIN_PROCEDIMIENTO'
    return t

def t_PR_MED_TEN_CENTRAL(t):
    r'MTC'
    return t

def t_PR_MED_DISPERSION(t):
    r'MD'
    return t

def t_PR_INDIVIDUO(t):
    r'INDIVIDUO'
    return t

def t_PR_DEVUELVE(t):
    r'devuelve'
    return t


#Lista De Simbolos Y operadores

t_RAIZ            = r'~'
t_POTENCIA        = r'\*\*'
t_ADICION         = r'\+'
t_SUSTRACCION     = r'-'
t_PRODUCTO        = r'\*'
t_DIVISION        = r'/'
t_SUMATORIA       = r'\+\+'
t_IGUAL           = r'='
t_OP_MENOR        = r'\<\:'
t_OP_MAYOR        = r'\:\>'
t_COMA            = r','
t_PARENTESIS_DER  = r'\('
t_PARENTESIS_IZQ  = r'\)'
t_CORCHETE_DER    = r'\['
t_CORCHETE_IZQ    = r'\]'
t_PUNTO           = r'\.'

def t_IGUAL_FUNC(t):
    r'equal'
    return t

def t_OP_IGUALDAD (t):
    r'=='
    return t

#FUNCIONES 

def t_Calc_MEDIA_ARITMETICA (t):
    r'MEDIA'
    return t

def t_Calc_MEDIANA (t):
    r'MEDIANA'
    return t

def t_Calc_MODA (t):
    r'MODA'
    return t

def t_Calc_DESV_ESTANDAR (t):
    r'DES_ESTANDAR'
    return t

def t_Calc_VARIANZA (t):
    r'VARIANZA'
    return t

def t_ORDENA (t):
    r'ORDENAR'
    return t

def t_AGREGA (t):
    r'AGREGAR'
    return t

def t_IMPRIME_DATOS (t):
    r'IMPRIME'
    return t

# OTROS

def t_COMENTARIOS(t):
    r'\/\*([^*]|\*[^\/])*(\*)+\/'
    t.lexer.lineno += t.value.count('\n')

def t_VARIABLE(t):
    r'\$\w+(\d\w)*'
    return t

def t_NUMEROS(t):
    r'\d+(\.\d+)?'

    if '.'in t.value:
        t.value = float(t.value)
    else:
        t.value = int(t.value)
    return t

lexer = lex.lex()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        script = sys.argv[1]
        scriptfile = open(script, 'r')
        scriptdata = scriptfile.read()
        lexer.input(scriptdata)

        reservadas = []
        operadores = []
        funciones = []
        otros = []


        NPr = 1
        NFun = 1
        NOp = 1
        Notr = 1
        
        while True:
            tok = lexer.token()
            if not tok:
                break

            if tok.type in ['PR_MUESTRA', 'PR_POBLACION', 'PR_CONTINUA', 'PR_DISCRETA', 'PR_MEZCLA', 'PR_PROCEDIMIENTO',
                            'PR_FIN_PROCEDIMIENTO', 'PR_MED_TEN_CENTRAL', 'PR_MED_DISPERSION', 'PR_INDIVIDUO','PR_DEVUELVE']:
                reservadas.append("|{: ^4}|{: ^10}|{: ^25}|{: ^25}|".format(NPr, tok.lineno, tok.type, tok.value).replace("|", '\033[96m|\033[0m'))
                NPr += 1
            elif tok.type in ['Calc_MEDIA_ARITMETICA','Calc_MEDIANA','Calc_MODA','Calc_DESV_ESTANDAR',
                            'Calc_VARIANZA','ORDENA','AGREGA','IMPRIME_DATOS']:
                funciones.append("|{: ^4}|{: ^10}|{: ^25}|{: ^25}|".format(NFun, tok.lineno, tok.type, tok.value).replace("|", '\033[96m|\033[0m'))
                NFun += 1
            elif tok.type in ['COMENTARIOS','NUMEROS','VARIABLE',]:
                otros.append("|{: ^4}|{: ^10}|{: ^25}|{: ^25}|".format(NOp, tok.lineno, tok.type, tok.value).replace("|", '\033[96m|\033[0m'))
                Notr+=1
            else:
                operadores.append("|{: ^4}|{: ^10}|{: ^25}|{: ^25}|".format(NOp, tok.lineno, tok.type, tok.value).replace("|", '\033[96m|\033[0m'))
                NOp += 1

        print ("\n\n                    Palabras reservadas encontradas\n")
        print('\033[92m'"+-------------------------------------------------------------------+"'\033[0m')
        print("|{: ^4}|{: ^10}|{: ^25}|{: ^25}|".format("No.", "Linea", "Token", "Palabra reservada").replace("|", '\033[92m|\033[0m'))
        print('\033[92m'"+-------------------------------------------------------------------+"'\033[0m')

        for item in reservadas:
            print(item)
            print('\033[96m'"+-------------------------------------------------------------------+"'\033[0m')

        print ("\n\n                      Funciones encontradas\n")
        print('\033[92m'"+-------------------------------------------------------------------+"'\033[0m')
        print("|{: ^4}|{: ^10}|{: ^25}|{: ^25}|".format("No.", "Linea", "Token", "Funcion").replace("|", '\033[92m|\033[0m'))
        print('\033[92m'"+-------------------------------------------------------------------+"'\033[0m')

        for item in funciones:
            print(item)
            print('\033[96m'"+-------------------------------------------------------------------+"'\033[0m')

        print ("\n\n                   Operadores y Simbolos encontrados\n")
        print('\033[92m'"+-------------------------------------------------------------------+"'\033[0m')
        print("|{: ^4}|{: ^10}|{: ^25}|{: ^25}|".format("No.", "Linea", "Token", "Operadores-Simbolos").replace("|", '\033[92m|\033[0m'))
        print('\033[92m'"+-------------------------------------------------------------------+"'\033[0m')

        for item in operadores:
            print(item)
            print('\033[96m'"+-------------------------------------------------------------------+"'\033[0m')

        print ("\n\n                        Otros datos encontrados \n")
        print('\033[92m'"+-------------------------------------------------------------------+"'\033[0m')
        print("|{: ^4}|{: ^10}|{: ^25}|{: ^25}|".format("No.", "Linea", "Token", "Valor").replace("|", '\033[92m|\033[0m'))
        print('\033[92m'"+-------------------------------------------------------------------+"'\033[0m')

        for item in otros:
            print(item)
            print('\033[96m'"+-------------------------------------------------------------------+"'\033[0m')

    else:
        print("+-------------------------------------------------+")
        print("|\033[92m Pasar el archivo de script TXT como parámetro:  \033[0m|")
        print("|\033[92m De esta Forma :                                 \033[0m|")
        print("|\033[95m python AnalizadorLexico.py <filename>.txt       \033[0m|")
        print("+-------------------------------------------------+")

