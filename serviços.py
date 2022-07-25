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

agendaserv= saveserv()


def cadastrar_servico():
  print ('~~'*30)
  print ("Bem vindo aos nossos serviços!")
  print ('~~'*30)
  
  while True:
      nome = input('informe seu nome para a consulta ')
      if validstring(nome):
        break
      else:
        print("nome invalido! ")


  while True:
    data = input('Que dia você gostaria para marcar sua consulta? ')
    if data_valida(data):
      break
    else:
      print('Data invalida!')

  while True:
        serv = input("O que você gostaria de marcar no nosso estabelecimento? 1 banho e tosa ou 2 consulta veterinaria? ")
        if serv == "1":
          serv = "Banho e tosa"
          break
        elif serv == "2":
          serv = "Consulta veterinária"
          break
        else:
          print('Numero invalido')
        
  while True:
      hora = ' '   
      hora = input('Escolha um horário para o atendimento do seu animal: Utilize as horas das 8:00 as 18:00 ')
      if validhora(hora):
        break
      else:
        print('hora invalida!')
    
        
    
      
  
  while True:
      cpf = input('Informe seu cpf: ')
      if cpf1(cpf):
        if cpf not in agendaserv:
          agendaserv[cpf] = [nome, serv, data, hora]
          print('Usuário cadastrado com sucesso!')
          # for i in range(agendaserv):
          print(agendaserv)
          print()
          savedata(agendaserv)
          break
        else:
          print("Usuario já cadastrado! ")
  input ('Tecle enter para continuar')
  menu_servicos()
        
    


def cancelar_servico():
  print('Bem vindos ao cancelamento de serviço!')
  while True:
    del_servico = ' '
    del_servico = input("Qual o chave do agendamento que você que deletar: ")
    if del_servico in agendaserv:
      del agendaserv[del_servico]
      print(f'O agendamento {del_servico} foi deletado')
      savedata(agendaserv)
      break
    else:
      print("Agendamento não encontrado: ")
  input("\n APERTE ENTER PARA VOLTAR AO MENU DO USUARIO")
  menu_servicos()

def lista_serv():
  os.system("cls")
  # for i in range(agendaserv):
  print (agendaserv)
  print()
  input ('Tecle enter para continuar! ')
  menu_servicos()
  



def menu_servicos():
  os.system('cls')
  print("#"*35)
  print('        MENU DE SERVIÇOS')
  print('#'*35)
  print("1. AGENDAR NOVO SERVIÇO")
  print("2. CANCELAR AGENDAMENTO ")
  print('3. LISTA DE SERVIÇo')
  print("0. SAIR")
  chip = ' '
  chip = input("\tO QUE VOCÊ DESEJA? \n ")
  while chip != '0':
    if chip == '1':
      cadastrar_servico()
    elif chip == '2':
      cancelar_servico()
    elif chip == '3':
      lista_serv()
    else:
      print('Opção inválida!')
      break

  
    
    
      
 
    

  