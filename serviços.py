import os
############ SERVIÇOS #################
  
def modulo_servicos():
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


  