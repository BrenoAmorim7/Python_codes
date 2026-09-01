import random

entrada = input ("digite o nome das pessoas presentes no sorteio SEPARADOS POR ESPAÇO\n").split()
    
    
contador = 1
while contador == 1:
    sorteio = random.choice(entrada)
    print(f"o sorteado foi o {sorteio}")
    contador = int(input("digite [1] para sortear outro nome ou [0] para finalizar\n"))