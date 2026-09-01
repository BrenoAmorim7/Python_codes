'''Desenvolva um algoritmo que leia o nome, a idade e o sexo de várias pessoas. O programa vai perguntar se o usuário quer ou não continuar. No final, mostre:
a) O nome da pessoa mais velha
b) O nome da mulher mais jovem
c) A média de idade do grupo
d) Quantos homens tem mais de 30 anos
e) Quantas mulheres tem menos de 18 anos '''

homem30 = 0
cont = 1
qnt = 1
idade_pessoavelha = 0
nome_pessoavelha = '?'
media = 0
mulherdemenor = 0
pessoas = 0
idade_mulherjovem = 100
nome_mulherjovem = '?'

while cont != 0:                     
    print(f"\t\033[33m{qnt}ª\033[m pessoa")
    nome = input(f"digite o nome da pessoa\n")
    while True:
                  
        try:                       
            idade = int(input("digite a \033[1;33midade/033[m dessa pessoa\n"))
            if idade > 0 or idade < 130:
                print("/033[1;34midade\033[m registrada!\n")
            
                break
        except:
                print("digite uma \033[1;31midade valida\033[m por favor\n")
                continue
    if idade > idade_pessoavelha:
                idade_pessoavelha = idade
                nome_pessoavelha = nome
    
    media += idade

    while True:
        
        sexo = input("digite o sexo \033[1;33m[M]\033[m para masculino e \033[1;33m[F]\033[m para feminino\n").upper()
        if sexo.isalpha() and (sexo == 'M') or (sexo == 'F'):
            break
        else:
            print("digite uma das letras indicadas por favor")
            continue
    if sexo == 'M':
        if idade > 30:
            homem30 += 1
            
    elif sexo == 'F':
        if idade < 18:
            mulherdemenor += 1
        if idade < idade_mulherjovem:
            idade_mulherjovem = idade
            nome_mulherjovem = nome 

        
    pessoas += 1
    qnt += 1
    while True:
        try:
            print("digite [1] para adicionar outra pessoa\n")
            print("digite [0] para encerrar e receber os resultados\n")
            cont = int(input("\n"))
            break
        except:
            print("digite somente NUMEROS [0] OU [1]!!!!!!")
            continue
media = media / pessoas

print(f"o nome da pessoa mais velha é {nome_pessoavelha}\n")
print(f"o nome da mulher mais jovem é {nome_mulherjovem}")
print(f"A media das idades em Geral é de {media:.2f} anos\n")
print(f"exatamente {homem30} homens tem mais de 30 anos\n")
print(f"exatamente {mulherdemenor} mulheres tem menos de 18 anos")        


    


