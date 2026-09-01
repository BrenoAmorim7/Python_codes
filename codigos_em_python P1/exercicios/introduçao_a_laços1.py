#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem
# caso o valor seja
# inválido e continue pedindo até que o usuário informe um valor válido

valor = float(input("digite um numero de 1 - 10\n"))

while (valor < 1) or (valor > 10):
    valor =float (input("digite um valor valido de 1 - 10\n"))
    print("numero invalido parceiro\n")

print(f"agora o numero e valido e é {valor:.0f}")