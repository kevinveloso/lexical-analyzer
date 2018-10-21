# Alunos: Fernando Souza (11218354) e Kevin Veloso (11318626)
import spacy
import re
import requests
import sys
from spacy.lang.pt.examples import sentences

TOKEN = 0
CLASS = 1


def project_syntactic(officialList):
    textoPoject(officialList)

def textoPoject(officialList):
    sentenca(officialList)

    if officialList[0][TOKEN] == '.':
        officialList.remove(officialList[0])

    if (len(officialList) > 0):
        textoPoject_(officialList)

    elif len(officialList) == 0:
        print('PROGRAMA FINALIZADO CORRETAMENTE')

def textoPoject_(officialList):
    textoPoject(officialList)

def sentenca(officialList):
    while officialList[0][TOKEN] is not '.':
        
        sintagma_nominal(officialList)

        sintagma_verbal(officialList)
        
        # if officialList[0][CLASS] == 'NOUN':
        #         officialList.remove(officialList[0])

        # elif officialList[0][CLASS] == 'DET':
        #     officialList.remove(officialList[0])
        #     if officialList[0][CLASS] == 'NOUN':
        #         officialList.remove(officialList[0])
        #         if officialList[0][CLASS] != 'VERB' and officialList[0][TOKEN] != '.':
        #             officialList.remove(officialList[0])

        # elif officialList[0][CLASS] == 'VERB':
        #     sintagma_verbal(officialList)
        
def sintagma_nominal(officialList):
    if officialList[0][CLASS] == 'NOUN':
        officialList.remove(officialList[0])

    elif officialList[0][CLASS] == 'DET':
        officialList.remove(officialList[0])
        if officialList[0][CLASS] == 'NOUN':
            officialList.remove(officialList[0])
            if officialList[0][CLASS] != 'VERB' and officialList[0][TOKEN] != '.':
                officialList.remove(officialList[0])



def sintagma_verbal(officialList):
    if officialList[0][CLASS] == 'VERB':
        officialList.remove(officialList[0])
        if officialList[0][CLASS] == 'ADV':
            officialList.remove(officialList[0])
            sintagma_verbal(officialList)
    else:
        sentenca(officialList)


    if len(officialList) > 0 and officialList[0][TOKEN] != '.' :
        sintagma_verbal(officialList)
        


nlp = spacy.load('pt_core_news_sm')

params = sys.argv[1:]
projectTable = list()
officialList = list()
# projectTable = open('./data/tabela.txt', 'w')

for item in params:
    doc = nlp(item)
    for token in doc:
        r = requests.get('http://www.dicionarioweb.com.br/' + token.text)
        if r.status_code == 404:
            sys.exit('palavra '+ token.text + ' esta escrita incorretamente')

        projectTable.append(token.text + ' ' + token.pos_ + ' ' + token.dep_ )
        # projectTable.write(token.text + ' ' + token.pos_ + ' ' + token.dep_ + '\n')

        # print(token.text, token.pos_, token.dep_)


texto = ''
for item in params:
    texto = texto + item + ' '
# print(params)
# print(texto)

r2 = requests.post('https://languagetool.org/api/v2/check', data={'text': texto, 'language': 'pt-br', 'enabledOnly': 'false'})
resp = r2.json()
concord = resp['matches'][0]['message']

isConcord = re.split(r'em Português do Brasil utiliza-se', concord)

if len(isConcord) == 1:
    sys.exit(concord)


print(projectTable)

for palavra in projectTable:
    palavra = re.split(r'\s', palavra)
    officialList.append(palavra)

print(officialList)

project_syntactic(officialList)


