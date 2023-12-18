# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 12:06:44 2022

@author: Simone
"""

from studioMedico import *
#from random import randint

NPAZIENTI=100
AGE_MIN=18
AGE_MAX=60
MIN_LEN_NOME=5
MAX_LEN_NOME=7
ALFABETO="abcdefghijklmnopqrstuvwxyz"

def nomeCasuale():
    nome=""
    lungNome=randint(MIN_LEN_NOME,MAX_LEN_NOME)
    for i in range(lungNome):
        nome+=ALFABETO[randint(0,len(ALFABETO)-1)]
    return nome

def genereCasuale():
    if randint(0,100)>50:
        return "F"
    else:
        return "M"
    
def cercanomeperlettera(Sdict, lettera):
    c={}
    for p in Sdict:
        if Sdict[p].nome[0] == lettera:
            c[p]=Sdict[p]
    return c


def etàmaggiore(Sdict):
    m={}
    max=0
    for p in Sdict:
        if Sdict[p].age > max:
            max=Sdict[p].age
            m[0]=Sdict[p]
    
    return m


def etàminore(Sdict):
    n={}
    min=60
    for p in Sdict:
        if Sdict[p].age < min:
            max=Sdict[p].age
            n[0]=Sdict[p]
    
    return n


   
# creo dizionario pazienti
S={}
for i in range(NPAZIENTI):
    S[i]=Paziente(nomeCasuale(),genereCasuale(),randint(AGE_MIN,AGE_MAX),False)

studio=Studio(S)
print(studio)
print("I vaccinati sono {}%".format(studio.percentualeVaccinati()))

studio.vaccinazioneSmart(100)
print("I vaccinati sono {}%".format(studio.percentualeVaccinati()))

ricerca=Studio(cercanomeperlettera(S, 'b'))
print(ricerca)

etàMaggiore=Studio(etàmaggiore(S))
print("il paziente con ètà maggiore è il " + str(etàMaggiore))

etàMinore=Studio(etàminore(S))
print("il paziente con ètà minore è il " + str(etàMinore))






