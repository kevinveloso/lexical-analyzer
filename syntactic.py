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

# ###
# #   Checa se a token eh um fator
# #   retorna true ou false
# ###
# def isFactor(token):
#     isFactor = False

 
#     if token[0][CLASS] == 'IDENTIFICADOR':
#         if token[1][TOKEN] == '(': 
#             if not isExpressionList(token):
#                 return False
#         isFactor = True

#     elif token[0][CLASS] == 'INTEGER' or token[0][CLASS] == 'REAL':
#         isFactor = True

#     elif token[0][TOKEN] == 'true' or token[0][TOKEN] == 'false':
#         isFactor = True

#     elif token[0][TOKEN] == '(':
#         isFactor = isExpression(token)

#     elif token[0][TOKEN] == 'not':
#         token.remove(token[0])
#         isFactor = isFactor(token)
    
#     return isFactor

# ###
# #   Checa se a token eh um termo
# #   retorna true ou false
# ###
# def isTerm(token):
#     isTerm = False

#     if len(token) = 0:
#         isTerm = True

#     if isFactor(token[0]):
#         token.remove(token[0])
        
#         if len(token) > 0:
#             if token[0][TOKEN] in multOperators:
#                 token.remove(token[0])
                
#                 if isFactor(token[0]) :
#                     token.remove(token[0])

#                     isTerm(token)
#         else:
#             isTerm = True

#     return isTerm

###
#   Checa se a token eh uma exprecao simples
#   retorna true ou false
###
# def isSimpleExpression(token):
#     isSimpleExp = False

#     if len(token) == 0:
#         isSimpleExp = True
#     elif token[0][TOKEN] in numberSignals:
#         token.remove(token[0])

#         if isTerm(token):
#             token.remove(token[0])
#             isSimpleExp = True
#         if
    

#     return isSimpleExp
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

                    if isExpression(line):
                        isVariableAttr = True
                        break

    return isVariableAttr

###
#   Checa se a linha eh uma expressao
#   retorna true ou false
###
def isExpression(line, flag = True):
    isExpression = False
    parenthesisCount = list()
    
    while line :

      if (line[0][TOKEN] in numberSignals) and (flag):
            line.remove(line[0])

            if (line[0][CLASS] == 'INTEGER') or (line[0][CLASS] == 'REAL'):
                line.remove(line[0])

                if (line[0][TOKEN] in relationalOperators) or (line[0][TOKEN] in addOperators) or (line[0][TOKEN] in multOperators):
                    line.remove(line[0])

                    if isExpression(line, False):
                        isExpression = True
                        break

                elif line[0][TOKEN] == ';' :
                    isExpression = True
                    break    

        elif (line[0][TOKEN] == 'not') and (flag) :
            line.remove(line[0])

            if isExpression(line, False):
                isExpression = True
                break

        elif ((line[0][TOKEN] == 'true') or (line[0][TOKEN] == 'false')) and (flag):
            line.remove(line[0])

            if line[0][TOKEN] == ';':
                isExpression = True
                break

        elif (line[0][CLASS] == 'INTEGER') or (line[0][CLASS] == 'REAL') or (line[0][TOKEN] in programVariables):
            line.remove(line[0])

            if (line[0][TOKEN] in relationalOperators) or (line[0][TOKEN] in addOperators) or (line[0][TOKEN] in multOperators):
                line.remove(line[0])

                if isExpression(line, False):
                    isExpression = True
                    break

            elif line[0][TOKEN] == ';' :
                isExpression = True 
                break

    #CONTROLE DE ABERTURA E FECHAMENTO DE PARENTESES
    parCount = 0

    for par in parenthesisCount :
        if par == '(':
            parCount += 1
        elif par == ')':
            parCount -=1
    
    if parCount is not 0:
        isExpression = False
            
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
            True
    return isCommand

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
        linesadad = [['valor1', 'IDENTIFICADOR', '7'], [':=', 'DELIMITADOR', '7'], ['10.3', 'REAL', '7'], [';','DELIMITADOR', '7']]
        print(isVariableAttr(linesadad))
    

        # while programLines:
        #     if(programLines[0][0][TOKEN] == 'begin'):
        #         print('comecou com begin')
        #         programLines.remove(programLines[0])    
        #     break    

                    

        # if(token(lista,linha) == '.')
        #     print("programa sem erros lexicos ou sintaticos")
