import random
print("SORTEADOR DE NOMES\n")
teste = 0
while True:
    if teste == 3:
        break
    n = input("digite os nomes dos alunos SEPARADOS POR ESPAÇO\n")
    nomes = n.split() # .split() retira os espaços 

    while True:
        qnt = int(input("digite a quantidade de nomes que deve ser sorteado\n"))
 
        if qnt > len(nomes): #a funçao len() significa a quantidade de nomes
            print("impossivel voce nao tem nomes o suficiente\n")
        elif qnt < 0:
            print("impossivel nao sortear ninguem\n")
        else:
            escolha = random.sample(nomes,qnt) 
            for nome in escolha:
                
                print(nome, end=(" "))   # o end=(" ") separa os prints por espaço sem quebrar linha
            print("\ndigite [1] para escolher outra quantidade de sorteados")
            print("digite [2] para escolher tudo do começo")
            print("digite [3] para encerrar o programa")
            teste = int(input(" "))
            if teste == 1:
                continue
            elif teste == 2:
                break
            else :
                teste = 3
                break