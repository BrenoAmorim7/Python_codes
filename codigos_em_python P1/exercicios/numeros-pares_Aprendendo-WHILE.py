'''faça um programa que printe somente os numeros pares de 0 ao numero que o usuario digitar'''
num = 0

cont = int(input("digite um numero maior que 0 para saber todos os numeros pares de 0 ate ele\n"))

while (num <= cont):
    if num % 2 == 0:
    
        print( f"{num}")
    num +=1