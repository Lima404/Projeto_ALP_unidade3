from main import *
import os
################# ESTOQUE ##################

chip = 0

estoque = {
            "001" : ["Ração para gato e cachorro", 9],
            "002" : ["Shampoo para cachorro", 14],
            "003" : ["Shampoo para gato", 34] }


def menu_estoque(chip):
  os.system ('cls')
  print()
  print("#"*35)
  print('        MENU DE ESTOQUE')
  print('#'*35)
  print()
  
  # NAVEGAÇÃO DO ESTOQUE
   
  print("1. VER LISTA DE ESTOQUE ")
  print("2. CADASTRAR PRODUTO DO ESTOQUE ")
  print("3. REMOVER PRODUTO DO ESTOQUE")
  print("4. VER PRODUTOS DO ESTOQUE EM FALTA")
  print ("0. SAIR")
  chip = input("\tO QUE VOCÊ DESEJA? \n ")

  return chip

############## modulo estoque ################

def cadastro_est():
  novoE = input('Digite um codigo referente a esse produto, caso não tenha um codigo crie um e nomeie a classe dele: ')
  if novoE == estoque['001']:
    estoque['001'] = novoE
    

def remover_est():
  delE = input('O que você deseja remover da lista:')
  estoque.remove (delE)

def modulo_estoque():
  menu_estoque(chip)
  while chip != "0":
    if chip == "1":
      print (estoque)
      input('tecle enter para continuar')
      menu_estoque()
    elif chip == "2":
      cadastro_est()
    elif chip == "3":
      remover_est()
    elif chip == "4":
      print()
    elif chip == "0":
      menu_principal()
    
    

def cadastro_estoque():
  novoE = input('O que você deseja cadastrar: ')
  estoque.append (novoE)

def remover_estoque():
  delE = input('O que você deseja remover da lista:')
  estoque.remove (delE)



info = []
  matr = input("Qual será o número da matrícula do usuario?  ")
  nome = input("Qual o nome do usuario ?  ")
  nome = nome.capitalize()
  info.append(nome)  
  idade = int(input("Adicione a idade do ususario: "))
  info.append(idade)
  agenda[matr] = info
  for matr in agenda:
    print()
    print ("Nome: \t",agenda[matr][0])
    print("Idade: \t",agenda[matr][1]) 
    print()
  print ("O usuario {} foi cadastrado com sucesso " .format(nome) )
  input("\n APERTE ENTER PARA CONTINUAR")

