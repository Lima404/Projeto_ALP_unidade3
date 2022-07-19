import os
from time import sleep
from usuario import menu1

chip = ' '
os.system ('cls')
while chip != '0':
  
  print()
  print("#"*35)
  print (' Agenda de serviços para pet-shop')
  print("#"*35)
  print()

  print()
  print("#"*35)
  print('          MENU PRINCIPAL')
  print('#'*35)
  print()

  print ('1. DADOS DE USUARIO [1]')
  print ('2. ESTOQUE DE PRODUTOS [2]')
  print ('3. SERVIÇOS [3]')
  print ('4. DADOS SOBRE O PROJETO [4]')
  print ('0. Sair do Menu [0]')

  chip = input("Por onde você quer navegar?  ")



  if chip == "1":
    menu1()
    
  elif chip == "2":
    modulo_estoque()
  elif chip == "3":
    modulo_servicos()
  elif chip == "4":
    modulo_projeto()
  
    
        
  print ("programa finalizado")


## ଘ(੭*ˊᵕˋ)੭