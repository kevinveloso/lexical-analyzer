# Alunos: Fernando Souza (11218354) e Kevin Veloso (11318626)
import spacy
import requests
from spacy.lang.pt.examples import sentences



nlp = spacy.load('pt_core_news_sm')
projectFile = open('./data/texto.txt', 'r')
# projectTable = open('./data/tabela.txt', 'w')

_file = nlp(projectFile.read())

print(_file.text)

for token in _file:
    r = requests.get('http://www.dicionarioweb.com.br/' + token.text)
    if r.status_code == 404:
        print('palavra '+ token.text + 'esta escrita incorretamente')
    print(token.text, token.pos_, token.dep_)