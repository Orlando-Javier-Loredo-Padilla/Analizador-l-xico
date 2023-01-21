"""
@author: Orlando
"""

import re 
file = open("read.py")

Identificador = re.compile(r'[a-zA-Z]+[\w]*') #Funcion para identificar cadenas
 
Entero = re.compile(r'[\d]')  #Funcion para identificar enteros

Real = re.compile(r'[\d]+\.[\d]+') #Funcion para identificar reales


operadores = {'+' : 'OpSuma tipo: 5','-' : 'OpSuma tipo: 5', #Reconocer operadores
             '*' : 'OpMul tipo: 6','/' : 'OpMul tipo: 6',
             '<' : 'OpRelac tipo: 7','<=' : 'OpRelac tipo: 7', '>': 'OpRelac tipo: 7', '>=' : 'OpRelac tipo: 7',
             '||' : 'OpOr tipo: 8', '&&' : 'OpAnd tipo: 9', '!' : 'OpNot tipo: 10',
             '==' : 'OpIgualdad tipo: 11', '!=' : 'OpIgualdad tipo: 11'}
operadores_key = operadores.keys()

simbolos = { ';' : '12', ',' : '13', '(' : '14' , ')' : '15',  #Reconocer simbolos
             '{' : '16', '}' : '17', '=' : '18' }
simbolos_key = simbolos.keys()

reservadas = {'if' : '19', 'while' : '20', 'return' : '21', #Reconocer palabras reservadas
              'else' : '22', '$': '23',
              'int' : '4','float' : '4', 'void': '4'}
reservadas_key = reservadas.keys()


dataFlag = False
a=file.read()           #leemos el .py
program = a.split("\n") #guardamos el tamaño del .py

print("Propiedades del texto \n")
for line in program:        #recorremos cada linea del .py
    tokens=line.split(' ')          #guardamos cada palabra de la linea 
    for token in tokens:            #evaluamos cada palabra
        if token in reservadas_key:
             print(token, "es una palabra reservada del tipo:", reservadas[token])        
        elif token in operadores_key:
             print(token, "es un operador", operadores[token]) 
        elif token in simbolos_key:
             print (token, "Es un simbolo del tipo:" , simbolos[token])         
        elif Real.match(token):
             print (token, "es un real del tipo: 2")                
        elif Entero.match(token):
             print (token, "es un entero del tipo: 1")      
        elif Identificador.match(token):
             print (token, "es un identificador del tipo: 0")
                    
    dataFlag=False
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _  _") 


#Funcion manual mediante ingresión de texto 

# linea = []  #Espacio para guardar nuestra cadena

# while (linea != 'exit'):  #Ciclo para usar la función con 'exit' finaliza
#     linea = input("Cadena a analizar: ")
#     print("Contenido de la linea:" , "\n" , linea)
#     tokens=linea.split(' ')
#     for token in tokens:
        
#         if token in reservadas_key:
#              print(token, "es una palabra reservada del tipo:", reservadas[token])        
#         elif token in operadores_key:
#              print(token, "es un operador", operadores[token]) 
#         elif token in simbolos_key:
#              print (token, "Es un simbolo del tipo:" , simbolos[token])         
#         elif Real.match(linea):
#             print (token, "es un real del tipo: 2")                
#         elif Entero.match(linea):
#             print (token, "es un entero del tipo: 1")      
#         elif Identificador.match(linea):
#             print (token, "es un identificador del tipo: 0")
            
#     print("\n-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+") 
