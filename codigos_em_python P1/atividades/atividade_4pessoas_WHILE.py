#programa que leia o nome idade e sexop de 4 pessoas
#mostrar media das idades, nome do homem mais velho
#quantas mulheres tem menos de 20 anos
idademaior = 0
mulheresmenos = 0
media = 0
i = 1
while i <= 4:
    print(f"\033[1;33m{i}\033[m pessoa")

    nome = input("digite o nome da pessoa\n")
    idade = int(input("digite a idade da pessoa\n"))
    sexo = str(input("digite \033[1;33m[M]\033[m para masculino e \033[1;33m[F]\033[m para feminino\n")).upper()
    media += idade
    if sexo == 'M':
        if idade > idademaior:
            idademaior = idade
            nomemaior = nome
    else:
        if idade < 20:
            mulheresmenos += 1
    i += 1
media = media / 4

print(f"\nO nome do homem mais velho é : {nomemaior}")
print(f"\na media de todas as idades é :{media}")
if mulheresmenos < 1:
    print("\nnao tinha nenhuma mulher com menos de 20 anos")
else:
    print(f"\ntinha exatamente {mulheresmenos} mulheres com menos de 20 anos")