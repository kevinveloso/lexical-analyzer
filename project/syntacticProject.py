# Alunos: Fernando Souza (11218354) e Kevin Veloso (11318626)

import sys
import re

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
    if officialList[0][CLASS] == 'NOUN':
            officialList.remove(official[0])
            # sintagma_nominal(officialList)

    elif officialList[0][CLASS] == 'DET':
        officialList.remove(officialList[0])
        if officialList[0][CLASS] == 'NOUN':
            officialList.remove(officialList[0])
            # sintagma_nominal(officialList)

    
    else:
        sintagma_verbal(officialList)

def sintagma_verbal(officialList):
    if officialList[0][CLASS] == 'VERB':
        officialList.remove(officialList[0])

    elif officialList[0][CLASS] == 'VERB':
        officialList.remove(officialList[0])
        if officialList[0][CLASS] == 'ADV':
            officialList.remove(officialList[0])
            sintagma_verbal(officialList)

    if len(officialList) > 0 :
        sintagma_verbal(officialList)
        






with open('./data/tabela.txt', 'r') as projectTable:
    sentence = projectTable.read()
    lista = re.split(r'\n', sentence)
    officialList = list()


    while '' in lista:
        lista.remove('')

    for palavra in lista:
        palavra = re.split(r'\s', palavra)
        officialList.append(palavra)
    

    # print(officialList)

    project_syntactic(officialList)
