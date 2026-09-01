##Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
loop = True
while loop:
    try:
        num = int(input("digite um numero inteiro positivo\n"))
        if num < 0 :
            print("por favor um numero POSITIVO")
        else:
            loop = False
    except:
        print("por favor digite numero inteiro positivo!!!!!!!")

tam = (len(num))
for tam in range(tam,0,-1):
    print(tam,end="")
