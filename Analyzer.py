import re

try:
    progFile = open('program.txt', 'r')
    table = open('table.txt', 'w')

    #keywords = ['program', 'var', 'integer', 'real',
    # 'boolean', 'procedure', 'begin', 'end', 'if',
    # 'then', 'else', 'while', 'do', 'not']
    delimiters = [';', '.', ':', '(', ')', ':=', ',']
    relationalOperators = ['=', '<', '>', '<=', '>=', '<>']
    addOperators = ['+', '-', 'or']
    multOperators = ['*', '/', 'and']

    program = progFile.read()

    rmvComents = re.sub(r'({.*\}|(\t))', "", program)     #  remove os comentarios e tabulacoes
    lines = re.split(r'\n', rmvComents)                 #  divide em linhas
    tokens = list()

    # lines eh string. isso aqui vai transformar em um array onde cada elemento eh uma linha
    for line in lines:
        tokens.append(re.split(r'\s|(<>)|(:=)|(;|\.|:|\(|\)|,|<|>|=|\+|\-|\*|\\)', line))

    # Remove os espacos em branco q ngm sabe pq eles foram parar la!!!
    for token in tokens:
        while ('') in token:
            token.remove('')
        while None in token:
            token.remove(None)

    count = 1

    # for line in lines:  REMOVER PQ NAO TA SERVINDO DE NADA// MAS AINDA PRECISA DIVIDIR MAIS PARA PEGAR OS ':'
    for token in tokens:
        tempToken = token

        for temp in tempToken:
            if re.match(r'[0-9].*', temp):
                aux = temp
                table.write(re.sub(r'[a-z].*|[A-Z].*', '', temp) + ' | ' + 'INTEIRO' + ' | '  + str(count) + '\n' )     
                temp = re.sub(r'[0-9]', '', aux)

            if temp in delimiters:
                table.write(temp + ' | ' + 'DELIMITADOR' + ' | '  + str(count) + '\n' )
            
            elif temp in addOperators:
                table.write(temp + ' | ' + 'OPERADOR DE ADICAO' + ' | ' + str(count) + '\n' )
            
            elif temp in multOperators:
                table.write(temp + ' | ' + 'OPERADOR MULTI' + ' | '  + str(count) + '\n' )
            
            elif temp in relationalOperators:
                table.write(temp + ' | ' + 'OPERADOR RELACIONAL' + ' | ' + str(count) + '\n' )

            else:
                if re.match(r'((program)|(var)|(integer)|(real)|(boolean)|(procedure)|(begin)|(end)|(if)|(then)|(else)|(while)|(do)|(not))', temp):
                    table.write(str(temp) + ' | ' + 'PALAVRA RESERVADA' + ' | ' + str(count) + '\n' )
                elif re.match(r'([0-9]+\.[0-9]*)', temp):
                    table.write(str(temp) + ' | ' + 'REAL' + ' | ' + str(count) + '\n' )
                elif re.match(r'[0-9]+', temp):
                    table.write(str(temp) + ' | ' + 'INTEIRO' + ' | ' + str(count) + '\n' )
                elif re.match(r'_*[a-zA-Z]+[0-9]*_*', temp):
                    table.write(str(temp) + ' | ' + 'IDENTIFICADOR' + ' | ' + str(count) + '\n' )
        count+=1
#Falta ainda tratar os casos como: 43huesa
#Falta tratar operador de atribuicao
#Falta tratar casos como: 45/2, 56-55, z=15, etc.
finally:
    progFile.close()
    table.close()   