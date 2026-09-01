print("calculador de media aritimetica preciso\n")

nome = input("primeiro digite seu nome\n")
while True:
    if (nome.isalpha()):
        print("nome valido!! prosseguindo!\n")
        break
    else:
        print("nome invalido, use apenas letras\n")
        nome = input("por favor digite um nome valido\n")
    continue

nota1 = input("digite sua primeira nota\n").strip().replace(',' , '.')
nota2 = input("digite sua segunda nota\n").strip().replace(',' , '.')
nota3 = input("digite sua terceira nota\n").strip().replace(',' , '.')

while True:
    if (nota1.isnumeric() ):
        num1 = float(nota1)
        print("primeira nota validada\n")
        
    else:
        print("por favor digite novamente a primeira nota")
        nota1 = input("digite novamente\n") 
        continue
        
    if (nota2.isnumeric() ):
        print("segunda nota validada\n")
        num2 = float(nota2)
    else:
        print("por favor digite novamente a segunda nota")
        nota2 = input("digite novamente\n").replace("," , ".")
        continue
    if (nota3.isnumeric() ):
        print("terceira nota validada")
        num3 = float(nota3)
        break
    else:
        print("por favor digite novamente a terceira nota")
        nota3 = input("digite novamente\n")  
        continue
media = ((num1) + (num2) + (num3)) / 3
if media >= 7 :
    print(f"\nseu nome é {nome}")
    print(f"\nsua media é de {media}")
    print("\nvoce foi aprovado!!!!")
elif media > 4 and media < 7 :
    print(f"\nseu nome é {nome}")
    print(f"\nsua media é de {media}")
    print("\nmedia baixa, porem com direito a FINAL!!!!")
else:
    print(f"\nseu nome é {nome}")
    print(f"\nsua media é de {media}")
    print("\nvoce esta reprovado!!!!")

