# Alunos: Fernando Souza (11218354) e Kevin Veloso (11318626)

import re

TOKEN = 0
CLASS = 1
LINE_NUMBER = 2

def isProgramId(line):
    isProgId = False
    
    if(line[0][TOKEN] == "program"):
            if(line[1][CLASS] == "IDENTIFICADOR"):
                if(line[2][TOKEN] == ";"):
                    isProgId = True
                    
    return isProgId

def isVarDeclaration(line):
    isVarDec = False
    variableTypes = ['integer', 'real', 'boolean']   
    if(line[0][CLASS] == 'IDENTIFICADOR'):  
        if(line[1][TOKEN] == ':'):
            if(line[2][TOKEN] in variableTypes):                      
                if(line[3][TOKEN] == ';'):
                    isVarDec = True

    return isVarDec                


# def nextToken(self):
#         if (self.index + 1) < len(self.list_tokens):
#             self.index += 1
#             return self.list_tokens[self.index]
#         else:
#             sys.exit("out range")

with open('./data/table.txt', 'r') as programTable:

    lines = programTable.read()
    lines = re.sub(r'( )', "", lines)

    lines = re.split(r'\s', lines)
    tokensList = list() #LINHAS DA TABELA
    linesList = list()

    programLines = list()

    while ('') in lines:
        lines.remove('')
   
    for line in lines:
        tokensList.append(re.split(r'\|',line))

    
    lastLine = '1'
    for line in tokensList: 

        if line[2] == lastLine:
            linesList.append(line) #ADICIONANDO NOVA PALAVRA NA LINHA
            lastLine = line[2]
        else:
            programLines.append(linesList) #FAZENDO FECHAMENTO DA ÚLTIMA LINHA
            linesList = list() #ZERANDO LISTA
            linesList.append(line) #INICIANDO LISTA COM PRIMEIRA PALAVRA DA NOVA LINHA
            lastLine = line[2] #INCREMENTANDO O LASTLINE
    programLines.append(linesList) #FAZENDO FECHAMENTO DA ÚLTIMA LINHA

#   Compilador deve começar com program
#   depois deve vir o identificador e em seguida
#   simbolo ; para indicar o fim do programa


    if(isProgramId(programLines[0])):
        
        programLines.remove(programLines[0])

        if(programLines[0][0][TOKEN] == 'var'):

            programLines.remove(programLines[0])
         
            while programLines: #CHECA PARA TODAS AS LINHAS SE VALEM COMO DEFINICAO DE TIPO DE VARIAVEL
                if(isVarDeclaration(programLines[0])):
                    programLines.remove(programLines[0])    
                elif (programLines[0][TOKEN] == 'begin'):
                    break
                else:
                    print('ERRO SINTATICO! TELA AZUL!')
                    break

        while programLines:
            if(programLines[0][0][TOKEN] == 'begin'):
                print('comecou com begin')
                programLines.remove(programLines[0])    
            break    

                    

        # if(token(lista,linha) == '.')
        #     print("programa sem erros lexicos ou sintaticos")
