#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';

nome = input("por favor informe seu nome\n")
idade = float(input("por favor informe sua idade\n"))
salario = float(input("informe seu salario\n"))
sexo = input("informe seu sexo (f) ou (m) \n")
civil = input("informe seu estado civil (s = solteiro) (c = casado) (v = viuvo) (d = divorciado)")

while len(nome) < 3:
    nome = input("nome com menos de 3 letras nao existe\n")

while (float(idade < 0)) or (float(idade > 150)):
    idade = float(input("digite uma idade valida por favor\n"))

while float(salario < 0):
        salario = float(input("nao tem como ganhar negativo parceiro\n"))

while (sexo != 'f') and (sexo != 'm') : 
    sexo = input("[m] ou [f] por favor , voce nao e um animal\n")

while (civil != 's') and (civil != 'c') and (civil != 'v') and (civil != 'd'):
    civil = input("por favor !,so tem essas opçoes [s],[c],[v],[d]\n")

print("\tessas sao todas as suas informaçoes\n")
print(f"nome = {nome}\n")
print(f"sua idade = {idade:.0f}\n")
print(f"seu salario = {salario:.1f}\n")
print(f"seu sexo = {sexo}\n")
print(f"estado civil = {civil}\n")
