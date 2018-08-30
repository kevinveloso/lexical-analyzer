# Alunos: Fernando Souza (11218354) e Kevin Veloso (11318626)

import re

def token(lista, linha):
    return lista[linha][0]

def classe(lista, linha):
    return lista[linha][1]

def linha(lista, linha):
    return lista[linha][2]

# def nextToken(self):
#         if (self.index + 1) < len(self.list_tokens):
#             self.index += 1
#             return self.list_tokens[self.index]
#         else:
#             sys.exit("out range")

with open('./data/table.txt') as f:
    lines = f.read()
    lines = re.sub(r'( )', "", lines)
    lines = re.split(r'\s', lines)
    lista = list()

    while ('') in lines:
        lines.remove('')
    
    for line in lines:
        lista.append(re.split(r'\|',line))
   
    linha = 0
    
#   Compilador deve começar com program
#   depois deve vir o identificador e em seguida
#   simbolo ; para indicar o fim do programa

    if(token(lista,linha) == "program"):
            linha +=1
            if(classe(lista,linha) == "IDENTIFICADOR"):
                linha +=1
                if(token(lista,linha) == ";"):
                    linha +=1
                    print("A baixo vem a braba grande!! :/")