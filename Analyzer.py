import re

try:
    progFile = open('program.txt', r)
    table = open('table.txt', w)

    #keywords = ['program', 'var', 'integer', 'real',
    # 'boolean', 'procedure', 'begin', 'end', 'if',
    # 'then', 'else', 'while', 'do', 'not']
    delimiters = [';', '.', ':', '(', ')', ':=', ',']
    relationalOperators = ['=', '<', '>', '<=', '>=', '<>']
    addOperators = ['+', '-', 'or']
    multOperators = ['*', '/', 'and']

    program = progFile.read()

    rmvComents = re.sub(r'({.*\}|(\\t))', "", program)     #  remove os comentarios e tabulacoes
    lines = re.split(r'(\\n)', rmvComents)                 #  divide em linhas
    tokens = list()

    for line in lines:
        tokens.append(re.split(r'\s', lines))

    count = 1

    for line in lines:
        for token in tokens:
            tempToken = re.split(r'(((and)|(or)|(<>)|(<=)|(>=)|(:=))|(\;|\.|\:|\(|\)|\,\+|-|=|\*|/|(<)|(>)))',token)

            for temp in tempToken:
                if temp in delimiters:
                    table.write(temp + ' | ' + 'DELIMITADOR' + ' | '  + count)
                
                elif temp in addOperators:
                    table.write(temp + ' | ' + 'OPERADOR DE ADIÇÃO' + ' | ' + count)
                
                elif temp in multOperators:
                    table.write(temp + ' | ' + 'OPERADOR MULTI' + ' | '  + count)
                
                elif temp in relationalOperators:
                    table.write(temp + ' | ' + 'OPERADOR RELACIONAL' + ' | ' + count)

                else:
                    if re.match(r'((program)|(var)|(integer)|(real)|(boolean)|(procedure)|(begin)|(end)|(if)|(then)|(else)|(while)|(do)|(not))', temp):
                        table.write(temp + ' | ' + 'PALAVRA RESERVADA' + ' | ' + count)
                    elif re.match(r'[0-9]', temp):
                        table.write(temp + ' | ' + 'INTEIRO' + ' | ' + count)
                    elif re.match(r'[0-9]\.[0-9]', temp):
                        table.write(temp + ' | ' + 'REAL' + ' | ' + count)
                    else:
                        table.write(temp + ' | ' + 'IDENTIFICADOR' + ' | ' + count)
        count++
#Falta ainda tratar os casos como: 43huesa
finally:
    progFile.close()
    table.close()   