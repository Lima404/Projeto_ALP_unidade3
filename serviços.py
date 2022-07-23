import os
import datetime
import pickle
from validacoes import *
from time import sleep
############ SERVIÇOS #################

def saveserv(): # Função para listar os itens dos arquivos
    try:
        listserv = open("listaserv.dat", "rb")
        agendaserv = pickle.load(listserv)
        listserv.close()
    except:
        listserv = open("listaserv.dat", "wb")
        listserv.close()

    return agendaserv


def savedata(agendaesto): # Função para gravar
    listesto = open("listaserv.dat", "wb")
    pickle.dump(agendaesto, listesto)
    listesto.close()

agendaserv= {}

def cadastrar_serviço():
  print()

def remover_serviço():
  print()

def alterar_data():
  print()

def remover_data():
  print()


def menu_serviços():
  os.system ('clear')
  print()
  print("#"*35)
  print('        MENU DE SERVIÇOS')
  print('#'*35)
  print()
  
  # NAVEGAÇÃO DO ESTOQUE
   
  print("1. CADASTRAR NOVO SERVIÇO")
  print("2. REMOVER SERVIÇO ")
  print("3. ALTERAR DATA DE SERVIÇO")
  print("4. REMOVER PRODUTO NO ESTOQUE ")
  print ("0. SAIR")
  chip = input("\tO QUE VOCÊ DESEJA? \n ")

  return chip

def modulo_servicos():
  chip = ' '
  while chip != '0':
    menu_serviços()
    chip = input("escolha uma opção: ")
    if chip == "1":
      cadastrar_serviço()
    elif chip == "2":
      remover_serviço()
    elif chip == "3":
      alterar_data()
    elif chip == "4":
      remover_data()
    

  