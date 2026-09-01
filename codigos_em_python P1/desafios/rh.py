dados = [
   ['TI','breno nunes ','000.000.000-00','14/02/2007'],
   [],
   []
]


import pandas as pd



def cpfvalido(cpf):
   if len(cpf) != 14:
       return False
  
#111.111.111-111
   if cpf[3] != '.' or cpf[7] != '.' or cpf[11] != '-':
       return False
   else:


       return True




def olhardata(data):


   if len(data) != 10:
       return False
  


   if data[2] != '/' or data[5] != '/':
       return False
   return True




def adicionar(nome,cpf,departamento):
   print("adionando outro usuario\n")
   while True:


       departamento = input('qual departamento?[TI],[FINANCEIRO],[RH],[GESTAO]').upper().strip()
       if departamento != 'TI' or departamento != 'RH' or departamento != 'GESTAO' or departamento != 'FINANCEIRO':
           continue
       else:
           break


   while True:


       nome = input("digite o nome do funcionario\n")
       if len(nome) < 2 or len(nome) > 100:
           continue
       else:
           break


   while True:


       cpf = input("digite o cpf do funcionario nesse formato!!! [xxx.xxx.xxx-xx]")
       cpfvalido(cpf)
       if cpfvalido(cpf) == False:
           continue
       else:
           break


   new = []
   new.append(departamento)
   print(new)
  
  


def cpfvalido(cpf):
   if len(cpf) != 14:
       return False
  
#111.111.111-111
   if cpf[3] != '.' or cpf[7] != '.' or cpf[11] != '-':
       return False
   else:


       return True




def olhardata(data):


   if len(data) != 10:
       return False
   


   if data[2] != '/' or data[5] != '/':
       return False
   return True




def adicionar():
   
   print("adionando outro usuario\n")
   while True:


       departamento = input('qual departamento? [TI],[FINANCEIRO],[RH],[GESTAO] \t ').upper().strip()
       if departamento != 'TI' and departamento != 'RH' and departamento != 'GESTAO' and departamento != 'FINANCEIRO':
           continue
       else:
           break


   while True:


       nome = input("digite o nome do funcionario\n")
       if len(nome) < 2 or len(nome) > 100:
           continue   
       else:
           break


   while True:


       cpf = input("digite o cpf do funcionario nesse formato!!! [xxx.xxx.xxx-xx]")
       cpfvalido(cpf)
       if cpfvalido(cpf) == False:
           continue
       else:
           break
   while True:
        data = input("digite a data de nascimento do funcionario no formato --> XX/XX/XXXX <---")

        if not olhardata(data):
            print("invalido")
            continue
       
        else:
            break
 
       

   new = []
   new.append(departamento)    
   new.append(nome)
   new.append(cpf)
   new.append(data)
    
   print(new)
  



  # escolha = int(input(""))




def menu():
   print('-' * 40)
   print("[1] exibir funcionario especifico por nome ")
   print("[2] exibir funcionario especifico por cpf")
   print("[3] adicionar novo funcionario")
   print("[4] mostrar listas de funcionarios por departamento ")
df = pd.DataFrame(dados)


print(df)
adicionar()


