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
    
    if(line[0][0][TOKEN] == "program"):
            if(line[0][1][CLASS] == "IDENTIFICADOR"):
                if(line[0][2][TOKEN] == ";"):
                    line.remove(line[0])

                    var_declaration(line)
                    subprograms_declaration(line)
                    composed_commands(line)
                    if (line[0][TOKEN] == '.'):
                        print('DEU BOM')
                        isProgId = True
                    
    return isProgId

###
#   Checa se a linha eh uma declaracao de variavel
#   retorna true ou false
###
def isVarDeclaration(line):
    isVarDec = False 
    
    programLines.remove(programLines[0])

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
#   Checa se a linha eh uma declaracao de subprogramas
#   retorna true ou false
###
def subprograms_declarations(line):
    subprograms_declarations__(line)


def subprograms_declarations__(line):
    if (subprogram_declaration(line)):
        if (line[0][0][TOKEN] == ';'):
            line.remove(line[0])
            subprograms_declarations__(line)
        else:
            sys.exit('1 - FALTOU ;')
    else:
        pass    

def subprogram_declaration(line):
    isSubDec = False
    if(line[0][0][TOKEN] == 'procedure'):
        line[0].remove(line[0][0])
        if(line[0][0][CLASS] == 'IDENTIFICADOR'):
            line[0].remove(line[0][0])
            arguments(line)
            if(line[0][0][TOKEN] == ';'):
                line.remove(line[0])
                var_declaration(line) # pode ser assim ao invez do de cima!! EU ACHO

                subprograms_declarations(line)
                composed_commands(line)
                isSubDec = True
                return isSubDec
            else:
                sys.exit('2 - FALTOU ;')

        else:
            sys.exit('3 - FALTOU IDENTIFICADOR')

def composed_commands(line):
    if (line[0][0][TOKEN] == 'begin'):
        line.remove(line[0])
        options_commands(line)
        if(line[0][0][TOKEN] == 'end'):
            return True
        else:
            sys.exit('FALTANDO COMANDO end')
    else:
        return False

def options_commands(line):
    list_commands(line)

def list_commands(line):
    command(line)
    list_commands__(line)

def list_commands__(line):
    if (line[0][0][TOKEN] == ';')
        line.remove(line[0])
        command(line)
        list_commands__(line)

def command(line):
    if (line[0][0][CLASS] == 'IDENTIFICADOR'):
        line[0].remove(line[0][0])
        if(line[0][0][TOKEN] == ':='):
            line[0].remove(line[0][0])
            expression(line)
            return
        else:
            sys.exit('15 - FALTOU :=')

    elif: 
        activation_procedure()
        pass
    elif composed_commands(line):
        pass
    else:
        reserved = line[0][0][TOKEN]

        if (reserved == 'if'):
            line[0].remove(line[0][0])
            expression(line)
            if(line[0][0][TOKEN] == 'then'):
                line[0].remove(line[0][0])
                command(line)
                else_part(line)
                return
            else:
                sys.exit('FALTOU O then')
        
        elif (reserved == 'while'):
            line[0].remove(line[0][0])
            expression(line)
            if(line[0][0][TOKEN] == 'do'):
                line[0].remove(line[0][0])
                command(line)
                return
            else:
                sys.exit('FALTOU O do')

        else:
            return False


def else_part(line):
    if(line[0][0][TOKEN] == 'else'):
        line.remove(line[0])
        command(line)

def activation_procedure(line):
    if (line[0][0][TOKEN] == 'IDENTIFICADOR'):
        line[0].remove(line[0][0])
        if(line[0][0][TOKEN] == '('):
            line[0].remove(line[0][0])
            list_expressions(line)
            if(line[0][0][TOKEN] == ')'):
                line[0].remove(line[0][0])
                return True
            else:
                sys.exit('FALTOU )')
        else:
            return True
    else:
        return False

def list_expressions(line):
    expression(line)
    list_expressions__(line)

def list_expressions__(line):
    if(line[0][0][TOKEN] == ','):
        line[0].remove(line[0][0])
        expression(line)
        list_expressions__(line)
        

def expression(line):
    if (simple_expression(line)):
        if(line[0][0][TOKEN] in relationalOperators):
            line[0].remove(line[0][0])
            simple_expression(line)
    else:
        sys.exit('ERROU EXPRESSAO')

def simple_expression(line):
    if (term(line)):
        simple_expression__(line)
        return True
    elif (line[0][0][TOKEN] in numberSignals):
        line[0].remove(line[0][0])
        term(line)
        simple_expression__(line)
        return True
    else:
        return False

def simple_expression__(line):
    if (line[0][0][TOKEN] in addOperators):
        line[0].remove(line[0][0])
        term(line)
        simple_expression__(line)

def op_relational(line):
    if (line[0][0][TOKEN] in relationalOperators):
        line[0].remove(line[0][0])
        return True
    else:
        return False

def op_aditive(line):
    if (line[0][0][TOKEN] in addOperators):
        line[0].remove(line[0][0])
        return True
    else:
        return False

def op_multiplicative(line):
    if (line[0][0][TOKEN] in multOperators):
        line[0].remove(line[0][0])
        return True
    else:
        return False
    
def term(line):
    if (factor(line)):
        term__(line)
        return True
    else:
        return False

def term__(line):
    if(op_multiplicative):
        factor(line)
        term__(line)

def factor(line):
    if (line[0][0][TOKEN] == 'IDENTIFICADOR'):
        line[0].remove(line[0][0])
        if (line[0][0][TOKEN] == '('):
            line[0].remove(line[0][0])
            list_expressions(line)
            if (line[0][0][TOKEN] == ')'):
                line[0].remove(line[0][0])
                return True
            else:
                sys.exit('FALTOU O )')
        else:
            return True

    elif (line[0][0][CLASS] == 'INTEIRO') or (line[0][0][CLASS] == 'REAL'):
        line[0].remove(line[0][0])
        return True
    elif (line[0][0][TOKEN] == 'true') or (line[0][0][TOKEN] == 'false'): 
        line[0].remove(line[0][0])
        return True
    elif (line[0][0][TOKEN] == '('):
        line[0].remove(line[0][0])
        expression(line)
        if (line[0][0][TOKEN] == ')'):
            line[0].remove(line[0][0])
            return True
        else:
            sys.exit('FALTOU O )')

    elif (line[0][0][TOKEN] == 'not'):
        line[0].remove(line[0][0])
        factor(line)
        return True






def var_declaration(line):
    if(line[0][0][TOKEN] == 'var'):
        line.remove(line[0])
        var_declaration_list(line)

def var_declaration_list(line):
    if(not list_identifiers(line)):
        if(line[0][0][TOKEN] == ':'):
            line[0].remove(line[0][0])
            if(line[0][0][TOKEN] in variableTypes):
                line[0].remove(line[0][0])
                if(line[0][0][TOKEN] == ';'):
                    line.remove(line[0])
                    var_declaration_list__(line)
                else:
                    sys.exit('7 - FALTOU ;')
            else:
                sys.exit('8 - ERROU O TIPO')
        else:
            sys.exit('9 - FALTOU :')
    else:
        sys.exit('10 - ERROU IDENDIFICAR')

def var_declaration_list__(line):
    if(list_identifiers(line)):
        if(line[0][0][TOKEN] == ':'):
            line[0].remove(line[0][0])
            if(line[0][0][TOKEN] in variableTypes):
                line[0].remove(line[0][0])
                if(line[0][0][TOKEN] == ';'):
                    line.remove(line[0])
                    var_declaration_list(line)
                else:
                    sys.exit('11 - FALTOU ;')
            else:
                sys.exit('12 - ERROU O TIPO')
        else:
            sys.exit('13 - FALTOU :')
    else:
        var_declaration_list(line)

def arguments(line):
    if(line[0][0][TOKEN] == '('):
        line[0].remove(line[0][0])
        list_parameters(line)
        
        if(line[0][0][TOKEN] == ')'):
            line.remove(line[0])
            pass
        else:
            sys.exit('4 - FALTOU ) ')

def list_parameters(line):
    list_identifiers(line)
    if (line[0][0][TOKEN] == ':'):
        line[0].remove(line[0][0])
        if(line[0][0][TOKEN] in variableTypes):
            line[0].remove(line[0][0])
            list_parameters__(line)
        else:
            sys.exit('6 - ERROU O TIPO')

def list_parameters__(line):
    if(line[0][0][TOKEN] == ';'):
        line[0].remove(line[0][0])
        if (not list_identifiers(line)) :
            if (line[0][0][TOKEN] == ':'):
                line[0].remove(line[0][0])
                if(line[0][TOKEN] in variableTypes):
                    line[0].remove(line[0][0])
                    list_parameters__(line)
            else:
                sys.exit('14 - ERRO SINTATICO :')

def list_identifiers(line):
    isListID = False
    if(line[0][0][CLASS] == 'IDENTIFICADOR'):
        line[0].remove(line[0][0])
        isListID = list_identifiers__(line)
        
    return isListID

def list_identifiers__(line):
    if (line[0][0][TOKEN] == ','):
        line[0].remove(line[0][0])
        if(line[0][0][CLASS] == 'IDENTIFICADOR'):
            line[0].remove(line[0][0])
            list_identifiers__(line)
            return True
    return False
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

            if line[0][TOKEN] == ';':
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
            True

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

    print(programLines)
    if(isProgramId(programLines)):
        print('a')
        # programLines.remove(programLines[0])

        # if(programLines[0][0][TOKEN] == 'var'):
        #     var_declaration(programLines)

        #     while programLines: #CHECA PARA TODAS AS LINHAS SE VALEM COMO DEFINICAO DE TIPO DE VARIAVEL
        #         if(isVarDeclaration(programLines[0])):
        #             programLines.remove(programLines[0])  
        #         elif (programLines[0][0][TOKEN] == 'begin'):
        #             break
        #         else:
        #             print('ERRO SINTATICO! TELA AZUL!')
        #             break

        # while programLines:
        #     if(programLines[0][0][TOKEN] == 'begin'):
        #         print('comecou com begin')
        #         programLines.remove(programLines[0])
        #         print(programLines)    
        #     break    
                    

        # if(token(lista,linha) == '.')
        #     print("programa sem erros lexicos ou sintaticos")
