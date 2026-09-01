import random
jogo = ['pedra','papel','tesoura']
loopgeral = True
while loopgeral:
    
    i = 0
    j = 0
    while i == 0:

        usuario = str(input("escolha entre \033[1;34m[pedra] [papel] [tesoura]\033[m\t")).upper()
        if not usuario.isalpha():
            print(" por favor digite apenas texto\t")
            i = 0
        elif usuario != 'PEDRA' and usuario != 'TESOURA' and usuario != 'PAPEL':
            print("por favor escolha apenas uma das 3 alternativas\t")
            i = 0
        else:
            i = 1
        
    computador = str(random.choice(jogo).upper())

    if usuario == 'PEDRA' and computador == 'PEDRA':
        print(f"\n {usuario} x {computador} = empate\n")

    elif usuario == 'PEDRA' and computador == 'TESOURA':
        print(f"\n {usuario} x {computador} = \033[1;32mvoce ganhou!!!\033[m\n")

    elif usuario == 'PEDRA' and computador == 'PAPEL':
        print(f"\n {usuario} x {computador} = computador ganhou!!!\n")

    elif usuario == 'TESOURA' and computador == 'PAPEL':
        print(f"\n {usuario} x {computador} = \033[1;32mvoce ganhou!!!\033[m\n")

    elif usuario == 'TESOURA' and computador == 'TESOURA':
        print(f"\n {usuario} x {computador} = empate!!!\n")

    elif usuario == 'TESOURA' and computador == 'PEDRA':
        print(f"\n {usuario} x {computador} = computador ganhou!!!\n")

    elif usuario == 'PAPEL' and computador == 'PAPEL':
        print(f"\n {usuario} x {computador} = empate!!!\n")

    elif usuario == 'PAPEL' and computador == 'TESOURA':
        print(f"\n {usuario} x {computador} = computador ganhou!!!\n")

    elif usuario == 'PAPEL' and computador == 'PEDRA':
        print(f"\n {usuario} x {computador} = \033[1;32mvoce ganhou!!!\033[m\n")
        
    print("\n digite 1 para jogar novamente e qualquer outro numero para encerrar o programa")

    while j == 0:
        try:
            num = int(input("\t"))
            j = 1
        except:
            print("\ndigite um numero por favor!!!!")
            j = 0
    if num == 1:
        loopgeral = True
    else:
        loopgeral = False
