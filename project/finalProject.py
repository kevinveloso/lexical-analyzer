# Alunos: Fernando Souza (11218354) e Kevin Veloso (11318626)
import spacy
import re
import requests
import sys
from spacy.lang.pt.examples import sentences
import os
from gtts import gTTS 


TOKEN = 0
CLASS = 1
LANGUAGE = 'pt'

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

#SEPARANDO O PONTO
if params[-1][-1:] == '.':
    params[-1] = params[-1][0:-1]
else:
    mytext = 'A frase deve terminar com um ponto final!'
    myobj = gTTS(text=mytext, lang=LANGUAGE, slow=False) 
    myobj.save("faltaponto_erro.mp3") 
    os.system("mpg321 faltaponto_erro.mp3") 
    sys.exit('A frase deve terminar com um ponto final!')

count = 1
for item in params:
    r = requests.get('http://www.dicionarioweb.com.br/' + item)
    
    if r.status_code == 404:
        mytext = 'A palavra ' + str(count) + ' está escrita incorretamente'
        myobj = gTTS(text=mytext, lang=LANGUAGE, slow=False) 
        myobj.save("escritaincorreta_erro.mp3") 
        os.system("mpg321 escritaincorreta_erro.mp3") 
        sys.exit('palavra '+ item + ' esta escrita incorretamente')

    count += 1

texto = ''
for item in params:
    texto = texto + item + ' '
texto = texto[0:-1] + '.'

doc = nlp(texto)
for token in doc:
    projectTable.append(token.text + ' ' + token.pos_ + ' ' + token.dep_ )

r2 = requests.post('https://languagetool.org/api/v2/check', data={'text': texto, 'language': 'pt-br', 'enabledOnly': 'false'})
resp = r2.json()

if len(resp['matches']) > 0:
    concord = resp['matches'][0]['message']

    isConcord = re.split(r'em Português do Brasil utiliza-se', concord)

    if len(isConcord) == 1:
        mytext = concord
        myobj = gTTS(text=mytext, lang=LANGUAGE, slow=False) 
        myobj.save("concordancia_erro.mp3") 
        os.system("mpg321 concordancia_erro.mp3") 

        sys.exit(concord)

for palavra in projectTable:
    palavra = re.split(r'\s', palavra)
    officialList.append(palavra)



project_syntactic(officialList)