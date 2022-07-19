import os
from time import sleep

agenda = {
            "2022111111" : ["Flavius", "25"],
             "2022111222": ["Janderson", '18'],
            "2022111333" : ["Xiko", '20'],
            
          }


########### USUARIO ###########

    


def cadastrar_usuario():
  os.system ('cls')
  print ("você escolheu cadastrar um novo usuario, vamos lá? \n")
  matr = input('Informe sua matricula: ')
  nome = input('Informa seu nome: ')
  idade = input('Informe sua idade: ')
  agenda[matr] = [nome, idade]
  print('Usuário cadastrado com sucesso!')
  print(agenda)
  sleep(5)
  


def procurar_usuario():
  nome = input('Qual nome você quer localizar: ')
  while True:
    if nome in agenda:
      print("Encontramos!")
      print(agenda)
      break
    
    else:
      print('Usuário não encontrado!')
      sleep(5)








def alterar_usuario():
  while True:
    alterar_dados = input("Qual o usuario que você gostaria de atualizar: dado pela matricula: ")
    if alterar_dados in agenda:
      
      novo_nome = input('Qual o novo nome: ')
      agenda[alterar_dados][0] = novo_nome
      nova_idade = input("Qual a nova idade: ")
      agenda[alterar_dados][1] = nova_idade
      print("Usuario atualizado com sucesso")

    else:
      print('Usuario não encontrado')
    
    input("\n APERTE ENTER PARA VOLTAR AO MENU DO USUARIO")
  





def apagar_usuario():
  del_usuario = str(input("Qual a matricula do usuario que vc que deletar: "))
  if del_usuario in agenda:
    del agenda[del_usuario]
    print(f'O usuario {del_usuario} foi deletado')
  else:
    print("Usuario não encontrado: ")
  input("\n APERTE ENTER PARA VOLTAR AO MENU DO USUARIO")

def lista_usuario():
  for mart in agenda :
    print()
    print ("Nome: \t",agenda[mart][0])
    print("Idade: \t",agenda[mart][1]) 
    print()
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
 


   