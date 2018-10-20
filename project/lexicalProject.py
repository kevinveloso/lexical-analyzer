# Alunos: Fernando Souza (11218354) e Kevin Veloso (11318626)
import spacy
import re
import requests
import sys
from spacy.lang.pt.examples import sentences



nlp = spacy.load('pt_core_news_sm')
projectFile = open('./data/texto.txt', 'r')
projectTable = open('./data/tabela.txt', 'w')
# oficialTable = list()
_file = nlp(projectFile.read())

print(_file.text)
r2 = requests.post('https://languagetool.org/api/v2/check', data={'text': _file.text, 'language': 'pt-br', 'enabledOnly': 'false'})
resp = r2.json()
concord = resp['matches'][0]['message']

isConcord = re.split(r'em Português do Brasil utiliza-se', concord)


if len(isConcord) == 1:
    sys.exit(concord)

for token in _file:
    r = requests.get('http://www.dicionarioweb.com.br/' + token.text)
    if r.status_code == 404:
        # print('palavra '+ token.text + 'esta escrita incorretamente')
        sys.exit('palavra '+ token.text + ' esta escrita incorretamente')
    # oficialTable.append(token.text + ' ' + token.pos_ + ' ' + token.dep_)
    projectTable.write(token.text + ' ' + token.pos_ + ' ' + token.dep_ + '\n')


# print(oficialTable)