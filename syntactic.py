# Alunos: Fernando Souza (11218354) e Kevin Veloso (11318626)

import re

TOKEN = 0
CLASS = 1
LINE_NUMBER = 2

variableTypes = ['integer', 'real', 'boolean'] 
programVariables = list()

numberSignals = ['-', '+']
relationalOperators = ['=', '<', '>', '<=', '>=', '<>']
addOperators = ['+', '-', 'or']
multOperators = ['*', '/', 'and']

###
#   Checa se a linha eh um identificador do programa
#   retorna true ou false
###
def isProgramId(line):
    isProgId = False
    
    if(line[0][TOKEN] == "program"):
            if(line[1][CLASS] == "IDENTIFICADOR"):
                if(line[2][TOKEN] == ";"):
                    isProgId = True
                    
    return isProgId

###
#   Checa se a linha eh uma declaracao de variavel
#   retorna true ou false
###
def isVarDeclaration(line):
    isVarDec = False 

    if(line[0][CLASS] == 'IDENTIFICADOR'):  
        if(line[1][TOKEN] == ':'):
            if(line[2][TOKEN] in variableTypes):                      
                if(line[3][TOKEN] == ';'):
                    isVarDec = True

        elif(line[1][TOKEN] == ','):
            i = 2
            while((line[i - 1][TOKEN] == ',') and (line[i][CLASS] == 'IDENTIFICADOR')):
                if(line[i + 1][TOKEN] == ':'):
                    if(line[i + 2][TOKEN] in variableTypes):                   
                        if(line[i + 3][TOKEN] == ';'):
                            isVarDec = True
                            break
                i += 2

        if(isVarDec):
            for token in line:
                if(token[CLASS] == 'IDENTIFICADOR'):
                    programVariables.append(token[TOKEN])

    return isVarDec     

###
#   Checa se a linha eh uma atribuicao de variavel
#   retorna true ou false
###
def isVariableAttr(line):
    isVariableAttr = False

    while line :

        if line[0][CLASS] == 'IDENTIFICADOR':
            if line[0][TOKEN] in programVariables:
                line.remove(line[0])

                if line[0][TOKEN] == ':=':
                    line.remove(line[0])

                    if isExpression(line[0]):
                        isVaribleAttr = True

    return isVariableAttr

###
#   Checa se a linha eh uma expressao
#   retorna true ou false
###
def isExpression(line, flag = True):
    isExpression = False

    while line :

        if (line[0][TOKEN] in numberSignals) and (flag):
            line.remove(line[0])

            if (line[0][CLASS] == 'INTEGER') or (line[0][CLASS] == 'REAL'):
                line.remove(line[0])

                if (line[0][TOKEN] in relationalOperators) or (line[0][TOKEN] in addOperators) or (line[0][TOKEN] in multOperators):
                    line.remove(line[0])

                    if isExpression(line, False):
                        isExpression = True

                elif line[0][TOKEN] == ';' :
                    isExpression = True    

        elif (line[0][TOKEN] == 'not') and (flag) :
            line.remove(line[0])

            if isExpression(line, False):
                isExpression = True

        elif ((line[0][TOKEN] == 'true') or (line[0][TOKEN] == 'false')) and (flag):
            line.remove(line[0])

            if line[0][TOKEN] == ';'
                isExpression = True

        elif (line[0][CLASS] == 'INTEGER') or (line[0][CLASS] == 'REAL') or (line[0][TOKEN] in programVariables):
            line.remove(line[0])

            if (line[0][TOKEN] in relationalOperators) or (line[0][TOKEN] in addOperators) or (line[0][TOKEN] in multOperators):
                line.remove(line[0])

                if isExpression(line, False):
                    isExpression = True

            elif line[0][TOKEN] == ';' :
                isExpression = True 
        
            
    return isExpression


###
#   Checa se a linha eh um comando
#   retorna true ou false
###
def isCommand(line):
    isCommand = False
    
    while line :

        if token[CLASS] == 'IDENTIFICADOR':
            if token[TOKEN] in programVariables:
                isCommand = isVariableAttr(line)
            else:
                break
        elif token[CLASS] == 'PALAVRARESERVADA':

###
#   ANALIZADOR SINTATICO
###
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
            programLines.append(linesList) #FAZENDO FECHAMENTO DA ULTIMA LINHA
            linesList = list() #ZERANDO LISTA
            linesList.append(line) #INICIANDO LISTA COM PRIMEIRA PALAVRA DA NOVA LINHA
            lastLine = line[2] #INCREMENTANDO O LASTLINE
    programLines.append(linesList) #FAZENDO FECHAMENTO DA ULTIMA LINHA

#   Compilador deve comecar com program
#   depois deve vir o identificador e em seguida
#   simbolo ; para indicar o fim do programa


    if(isProgramId(programLines[0])):
        
        programLines.remove(programLines[0])

        if(programLines[0][0][TOKEN] == 'var'):

            programLines.remove(programLines[0])
         
            while programLines: #CHECA PARA TODAS AS LINHAS SE VALEM COMO DEFINICAO DE TIPO DE VARIAVEL
                if(isVarDeclaration(programLines[0])):
                    programLines.remove(programLines[0])  
                elif (programLines[0][0][TOKEN] == 'begin'):
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
