import pickle
import os
from validacoes import *
from time import sleep




########### USUARIO ###########

def savearquivo(): # Função para listar os itens dos arquivos
    try:
        listclient = open("listaclient.dat", "rb")
        agenda1 = pickle.load(listclient)
        listclient.close()
    except:
        listclient = open("listaclient.dat", "wb")
        listclient.close()

    return agenda1


def savedados(agenda1): # Função para gravar
    listclient = open("listaclient.dat", "wb")
    pickle.dump(agenda1, listclient)
    listclient.close()
    
agenda1 = savearquivo()

def cadastrar_usuario():
  os.system ('cls')
  print ("você escolheu cadastrar um novo usuario, vamos lá? \n")

  while True:
      nome = input('Informe seu nome: ')
      if validstring(nome):
        break
      else:
        print("nome invalido! ")

  while True:
    idade = input('Informe seu idade: ')
    if validnum(idade):
      break
    else:
      print("idade invalida! ")

  while True:
      pet = input('Informe o tipo do seu pet: (Ex. Cachorro / Gato) ')
      if validstring(pet):
        break
      else:
        print("nome invalido! ")

  petdesc = input('Me fale um pouco do seu pet ')

  while True:
    cpf = input('Informe seu cpf: ')
    if cpf not in agenda1:
      agenda1[cpf] = [nome, idade, pet, petdesc]
      print('Usuário cadastrado com sucesso!')
      print(agenda1)
      savedados(agenda1)
      break
    else:
      print("Usuario já cadastrado! ")
  input ('Tecle enter para continuar')
  
  
  


def procurar_usuario():
  cpf = input('Qual o cpf você quer localizar: ')
  while True:
    if cpf not in agenda1:
      print ('usuario não encontrado')
      break
    else:
      print (agenda1[cpf])
      break
  input("tecle enter para continuar")





def alterar_usuario():
  while True:
    alterar_dados = input("Qual o usuario que você gostaria de atualizar: (localize pelo CPF:) ")
    if alterar_dados in agenda1:
      
      novo_nome = input('Qual o novo nome: ')
      agenda1[alterar_dados][0] = novo_nome

      nova_idade = input("Qual a nova idade: ")
      agenda1[alterar_dados][1] = nova_idade

      tipo_pet = input("Qual o tipo do pet: ")
      agenda1[alterar_dados][2] = tipo_pet

      desc_pet = input("Adcione uma nova descrição para o pet: ")
      agenda1[alterar_dados][3] = desc_pet
      print("Usuario atualizado com sucesso")
      savedados(agenda1)
      break

    else:
      print('Usuario não encontrado')
      break
    
  input("\n APERTE ENTER PARA VOLTAR AO MENU DO USUARIO")
  


def apagar_usuario():
  while True:
    del_usuario = input("Qual o cpf do usuario que vc que deletar: ")
    if del_usuario in agenda1:
      del agenda1[del_usuario]
      print(f'O usuario {del_usuario} foi deletado')
      savedados(agenda1)
      break
    else:
      print("Usuario não encontrado: ")
  input("\n APERTE ENTER PARA VOLTAR AO MENU DO USUARIO")




def lista_usuario():
    print(agenda1, end=' ')
    input("\n APERTE ENTER PARA VOLTAR AO MENU DO USUARIO")
  
################# mudulo usuario ##############
def menu1():
  usuario = ' '
  while usuario != '0':
      os.system ('cls')
      print()
      print("#"*35)
      print('        MENU DE USUARIO')
      print('#'*35)
      print()
      print("\tO QUE VOCÊ DESEJA? \n ")
      print("1. Cadastrar usuario ")
      print("2. Procurar usuario ")
      print("3. Alterar dados de usuario")
      print("4. Apagar Usuario")
      print("5. Lista de usuarios")
      print("0. Voltar") 
      usuario = input("escolha uma opção: ")
      if usuario == "1":
        cadastrar_usuario()
      elif usuario == "2":
        procurar_usuario()
      elif usuario == "3":
        alterar_usuario()
      elif usuario == "4":
        apagar_usuario()
      elif usuario == "5":
        lista_usuario()
 


   