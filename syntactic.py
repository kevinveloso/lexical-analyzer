# Alunos: Fernando Souza (11218354) e Kevin Veloso (11318626)

import re
import sys

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
def syntactic_analyzer(line):
    
    if(line[0][0][TOKEN] == "program"):
            if(line[0][1][CLASS] == "IDENTIFICADOR"):
                if(line[0][2][TOKEN] == ";"):
                    line.remove(line[0])
                    var_declaration(line)

                    if(line[0][0][TOKEN] == 'procedure'):
                        subprograms_declarations(line)
                    elif(line[0][0][TOKEN] == 'begin'):
                        composed_commands(line)

                    if (line[0][0][TOKEN] == '.'):
                        print('---PROGRAMA SINTATICAMENTE CORRETO---')                    

def subprograms_declarations(line):
    subprograms_declarations__(line)

def subprograms_declarations__(line):
    if (subprogram_declaration(line)):
        if (line[0][0][TOKEN] == ';'):
            line.remove(line[0])
            subprograms_declarations__(line)
        elif(line[0][0][TOKEN] == '.'):
            pass
        else:
            sys.exit('1 - ERRO SINTATICO: ; ESPERADO')
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

                if(line[0][0][TOKEN] == 'var'):
                    var_declaration(line)
                if(line[0][0][TOKEN] == 'procedure'):
                    subprograms_declarations(line)
                if(line[0][0][TOKEN] == 'begin'):
                    composed_commands(line)

                return isSubDec
            else:
                sys.exit('2 - ERRO SINTATICO: ; ESPERADO')

        else:
            sys.exit('3 - ERRO SINTATICO: IDENTIFICADOR ESPERADO')

def composed_commands(line):
    if (line[0][0][TOKEN] == 'begin'):
        line.remove(line[0])
        options_commands(line)

        if(line[0][0][TOKEN] == 'end'):
            line[0].remove(line[0][0])

            if (len(line[0]) == 0):
                line.remove(line[0])
            return True
        else:
            sys.exit('4 - ERRO SINTATICO: COMANDO end ESPERADO')
    else:
        return False

def options_commands(line):
    list_commands(line)

def list_commands(line):
    command(line)
    list_commands__(line)

def list_commands__(line):
    if (line[0][0][TOKEN] == ';'):
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
            sys.exit('5 - ERRO SINTATICO: := ESPERADO')

    elif activation_procedure(line): 
        pass
    elif composed_commands(line):
        pass
    else:
        reserved = line[0][0][TOKEN]
        #VER IF TIPO C
        if (reserved == 'if'):
            line[0].remove(line[0][0])
            expression(line)
            if(line[0][0][TOKEN] == 'then'):
                line.remove(line[0])
                command(line)
                else_part(line)
                return
            else:
                sys.exit('6 - ERRO SINTATICO: COMANDO then ESPERADO')
        
        elif (reserved == 'while'):
            line[0].remove(line[0][0])
            expression(line)
            if(line[0][0][TOKEN] == 'do'):
                line.remove(line[0])
                command(line)
                return
            else:
                sys.exit('7 - ERRO SINTATICO: COMANDO do ESPERADO')
        #DO WHILE
        # elif (reserved == 'do'):
        #     line.remove(line[0])
        #     command(line)

        #     if(line[0][0][TOKEN] == ';'):
        #         line.remove(line[0])

        #     if (line[0][0][TOKEN] == 'while'):
        #         line[0].remove(line[0][0])
        #         expression(line)
        #         return

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
                sys.exit('8 - ERRO SINTATICO: ) ESPERADO')
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
        sys.exit('9 - ERRO SINTATICO: EXPRESSAO ESPERADO')

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
    if(op_multiplicative(line)):
        factor(line)
        term__(line)

def factor(line):
    if (line[0][0][CLASS] == 'IDENTIFICADOR'):
        line[0].remove(line[0][0])
        
        if (line[0][0][TOKEN] == '('):
            line[0].remove(line[0][0])
            list_expressions(line)
            if (line[0][0][TOKEN] == ')'):
                line[0].remove(line[0][0])
                return True
            else:
                sys.exit('10 - ERRO SINTATICO: ) ESPERADO')
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
            sys.exit('11 - ERRO SINTATICO: ) ESPERADO')

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
                    sys.exit('12 - ERRO SINTATICO: ; ESPERADO')
            else:
                sys.exit('13 - ERRO SINTATICO: TIPO INVALIDO')
        elif (line[0][0][TOKEN] == 'procedure' or line[0][0][TOKEN] == 'begin'):
            pass
        else:
            sys.exit('14 - ERRO SINTATICO: : ESPERADO')
    else:
        sys.exit('15 - ERRO SINTATICO: IDENTIFICADOR INVALIDO')

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
                    sys.exit('16 - ERRO SINTATICO: ; ESPERADO')
            else:
                sys.exit('17 - ERRO SINTATICO: TIPO INVALIDO')
        else:
            sys.exit('18 - ERRO SINTATICO: : ESPERADO')
    else:
        var_declaration_list(line)

def arguments(line):
    if(line[0][0][TOKEN] == '('):
        line[0].remove(line[0][0])
        list_parameters(line)
        
        if(line[0][0][TOKEN] == ')'):
            line[0].remove(line[0][0])
            pass
        else:
            sys.exit('19 - ERRO SINTATICO: ) ESPERADO')

def list_parameters(line):
    list_identifiers(line)
    if (line[0][0][TOKEN] == ':'):
        line[0].remove(line[0][0])
        if(line[0][0][TOKEN] in variableTypes):
            line[0].remove(line[0][0])
            list_parameters__(line)
        else:
            sys.exit('20 - ERRO SINTATICO: TIPO INVALIDO')

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
                sys.exit('21 - ERRO SINTATICO: : ESPERADO')

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

    syntactic_analyzer(programLines)