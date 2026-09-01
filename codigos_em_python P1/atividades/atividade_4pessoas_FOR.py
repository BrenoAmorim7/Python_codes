#programa que leia o nome idade e sexop de 4 pessoas
#mostrar media das idades, nome do homem mais velho
#quantas mulheres tem menos de 20 anos
idademaior = 0
mulheresmenos = 0
media = 0
 
for i in range (1,5):
    print(f" {i} pessoa\n")
    nome = str(input("digite o nome da pessoa \n"))
    idade = int(input("digite a idade da pessoa\n"))
    sexo = input("digite o sexo da pessoa [M] ou [F]\n").upper() 
    media += idade 
    if sexo == 'M' :
        if idade > idademaior:
            nomemaior = nome
            idademaior = idade
            
    else :
        if idade < 20:
            mulheresmenos += 1
            
media = media / 4

print(f"\nmedia de idades : \033[1;33m{media:.1f}\033[m")
print(f"homem mais velho : \033[1;33m{nomemaior}\033[m")
if mulheresmenos > 0:
    print(f"quantidade de mulheres que tem menos de 20 anos : \033[1;33m{mulheresmenos}")
else:
    print("\033[1;31mnenhuma\033[m mulher tem menos doque 20 anos de idade")
