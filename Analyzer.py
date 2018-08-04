                                                                                                                                                                                                                                                
try:
    progFile = open('program.txt', r)
    table = open('table.txt', w)



    keywords = ['program', 'var', 'integer', 'real', 'boolean', 'procedure', 'begin', 'end', 'if', 'then', 'else', 'while', 'do', 'not']
    delimiters = [';', '.', ':', '(', ')', ':=', ',']
    relationalOperators = ['=', '<', '>', '<=', '>=', '<>']
    addOperators = ['+', '-', 'or']
    multOperators = ['*', '/', 'and']

    program = progFile.read()
    noComents = re.sub(r'({.*\}|(\\t))',"",program)     #   remove os comentarios e tabulacoes
    lines = re.split(r'(\\n)',noComents)                 #   divide em linhas
    tokens = re.split(r'\s',lines)
    count = 1

    #tem q verficar se houve um \n pra incrementar o count e remover ele da lista
    for line in lines:
        for token in tokens:
            tempToken = re.split(r'(((and)|(or)|(<>)|(<=)|(>=)|(:=))|(\;|\.|\:|\(|\)|\,\+|-|=|\*|/|(<)|(>)))',token)

            exemploparaagenteapagardepoisessecarai=[>,43hue,amae,program,:,=]
            for temp in tempToken:
                if temp in delimiters:
                    table.write(temp + '|' + 'DELIMITADOR' + '|'  + count)
                
                elif temp in addOperators:
                    table.write(temp + '|' + 'OPERADOR DE ADIÇÃO' + '|' + count)
                
                elif temp in multOperators:
                    table.write(temp + '|' + 'OPERADOR MULTI' + '|'  + count)
                
                elif temp in relationalOperators:
                    table.write(temp + '|' + 'OPERADOR RELACIONAL' + '|' + count)

                else:
                    if re.match(r'((program)|(var)|(integer)|(real)|(boolean)|(procedure)|(begin)|(end)|(if)|(then)|(else)|(while)|(do)|(not))', temp) :
                        table.write(temp + '|' + 'PALAVRA RESERVADA' + '|' + count)
                    
        count+=1


    
finally:
    progFile.close()
    table.close()   