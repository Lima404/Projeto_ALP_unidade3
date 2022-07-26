import pickle
import os
from validacoes import *
from time import sleep




########### SALVAMENTO DE ARQUIVOS ###########

def saveestoque(): # Função para listar os itens dos arquivos
    try:
        listesto = open("listaestoque.dat", "rb")
        agendaesto = pickle.load(listesto)
        listesto.close()
    except:
        listesto = open("listaestoque.dat", "wb")
        listesto.close()

    return agendaesto


def savedados(agendaesto): # Função para gravar
    listesto = open("listaestoque.dat", "wb")
    pickle.dump(agendaesto, listesto)
    listesto.close()

agendaesto= saveestoque()


def lista_estoque():
    os.syatem('cls')
    print(agendaesto)
    input("Tecle enter para voltar!")

def cadastro_estoque():
  os.system ('cls')
  print ("você escolheu cadastrar itens no estoque, vamos lá? \n")
  item = input('Informe um item que deseja cadastrar: ')
  quantidade = int(input('Informe a quantidade que será cadastrada: '))


  while True:
    id = " "
    id = input('Informe o id do produto: ')
    if id not in agendaesto:
      agendaesto[id] = [item, quantidade]
      print('Item cadastrado com sucesso!')
      print(agendaesto)
      savedados(agendaesto)
      break
  input ('Tecle enter para continuar')

def alterar_estoque():
    os.system('cls')
    chave = input("digite o id do produto em que você quer alterar a quantidade no estoque: ")
    subs = input("Você deseja acrescentar ou retirar este produto do estoque?\n [1] para acrescentar e [2] para retirar\n")
    if chave in agendaesto:
        cont = agendaesto[chave][1]
        numero = int(input('Quanto você gostaria de alterar desse item no estoque: '))    
            
        while True:    
            if subs == '1':
                soma =  cont + numero
                agendaesto[chave][1] = soma
                print(agendaesto[chave][1])
                savedados(agendaesto)
                break
            
            if subs == '2':
                sub = cont - numero
                agendaesto[chave][1] = sub
                print(agendaesto[chave][1])
                savedados(agendaesto)
                break
            else:
                print('Número inválido')
        input("TECLE ENTER PARA CONTINUAR!")    


def remover_estoque():
    while True:
        del_item = input("Qual o codigo do item que vc que deletar: ")
        if del_item in agendaesto:
            del agendaesto[del_item]
            print(f'O item {del_item} foi deletado')
            savedados(agendaesto)
            break
        else:
            print("item não encontrado: ")
    input("\n APERTE ENTER PARA VOLTAR AO MENU DO ESTOQUE!")


def menu_estoque():
  os.system ('cls')
  print()
  print("#"*35)
  print('        MENU DE ESTOQUE')
  print('#'*35)
  print()
  
  # NAVEGAÇÃO DO ESTOQUE
   
  print("1. LISTAR OS PRODUTOS DO ESTOQUE")
  print("2. CADASTRAR NOVO PRODUTO DO ESTOQUE ")
  print("3. ALTERAR QUANTIDADE DO PRODUTO NO ESTOQUE")
  print("4. REMOVER PRODUTO NO ESTOQUE ")
  print ("0. SAIR")
  chip = input("\tO QUE VOCÊ DESEJA? \n ")

  return chip

def modulo_estoque():
    chip = " "
    while chip != 0:
        key = "203040"
        chave = input('Você precisa digitar a chave de acesso para navegar nessa opção, Qual sua chave de acesso: ')
        if chave == key:
            chip = menu_estoque()
            if chip == "1":
                print (agendaesto)
                input('tecle enter para continuar')
                menu_estoque()
            elif chip == "2":
                cadastro_estoque()
            elif chip == "3":
                alterar_estoque()
            elif chip == "4":
                remover_estoque()
            break
        else:
            print("Acesso Negado")
            