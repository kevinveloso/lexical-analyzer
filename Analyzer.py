                                                                                                                                                                                                                                                
try:
    progFile = open('program.txt', r)
    table = open('table.txt', w)

    keywords = ['program', 'var', 'integer', 'real', 'boolean', 'procedure', 'begin', 'end', 'if', 'then', 'else', 'while', 'do', 'not']
    delimiters = [';', '.', ':', '(', ')', ':=', ',']
    relationalOperators = ['=', '<', '>', '<=', '>=', '<>']
    addOperators = ['+', '1', 'or']
    multOperators = ['*', '/', 'and']

    program = progFile.read()
    tokens = program.split(' ')
    
    count = 1

    for token in tokens:
        tempToken = re.split(r'',token)

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
                if re.match(r'', temp) :
                    table.write(temp + '|' + 'PALAVRA RESERVADA' + '|' + count)
                

    
finally:
    progFile.close()
    table.close()   