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


def savedata(agendaserv): # Função para gravar
    listesto = open("listaserv.dat", "wb")
    pickle.dump(agendaserv, listesto)
    listesto.close()

agendaserv= {}


def cadastrar_servico():
  print ('~~'*30)
  print ("Bem vindo aos nossos serviços!")
  print ('~~'*30)
  input("teste")
  
    while True:
      nome = input('informe seu nome para a consulta')
      if validstring(nome):
        break
      else:
        print("nome invalido! ")
    
    data = input('Que dia você gostaria para marcar sua consulta?')

    while True:
        serv = input("O que você gostaria de marcar no nosso estabelecimento? 1 banho e tosa ou 2 consulta veterinaria?")
        if serv == "1":
          serv = "banho e tosa"
        elif serv == "2":
          serv = "consulta veterinaria"
          break
        else:
          print('Numero invalido')
        
    while True:   
      hora = input ('Escolha um horário para a tosa do seu animal: Utilize as horas das 8:00 as 18:00 ')
      if hora in validnum():
        break
      else:
        print('numero invalido')
      
  
    while True:
      cpf = input('Informe seu cpf: ')
      
      if cpf not in agendaserv:
        agendaserv[cpf] = [nome, serv, data, hora,]
        print('Usuário cadastrado com sucesso!')
        print(agendaserv)
        saveserv(agendaserv)
        break
      else:
        print("Usuario já cadastrado! ")
    input ('Tecle enter para continuar')
        
    


def cancelar_servico():
  while True:
    del_servico = input("Qual o chave do agendamento que você que deletar: ")
    if del_servico in agendaserv:
      del agendaserv[del_servico]
      print(f'O agendamento {del_servico} foi deletado')
      saveserv(agendaserv)
      break
    else:
      print("Agendamento não encontrado: ")
  input("\n APERTE ENTER PARA VOLTAR AO MENU DO USUARIO")



def menu_servicos():
  os.system('cls')
  print()
  print("#"*35)
  print('        MENU DE SERVIÇOS')
  print('#'*35)
  print()
  print("1. AGENDAR NOVO SERVIÇO")
  print("2. CANCELAR AGENDAMENTO ")
  print("0. SAIR")
  chip = input("\tO QUE VOCÊ DESEJA? \n ")
  while chip != '0':
    chip1 = ' '
    menu_servicos()
    chip1 = input("escolha uma opção: ")
    if chip1 == "1":
      cadastrar_servico()
    elif chip1 == "2":
      cancelar_servico()
 
    

  