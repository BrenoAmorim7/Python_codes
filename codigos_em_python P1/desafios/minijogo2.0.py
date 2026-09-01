import random

amarelo = "\033[1;33m"
azul = "\033[1;34m"
verde = "\033[1;32m"
finalizar = "\033[m"
vermelho = "\033[1;31m"

jogo = {

"PEDRA" : "TESOURA",
"PAPEL" : "PEDRA",
"TESOURA" : "PAPEL"

}

opcoes = list(jogo.keys())

while True:

    while True:

        usuario = input(f"escolha entre {azul}[PEDRA] [PAPEL] [TESOURA] {finalizar}\n").upper().strip()

        if usuario in opcoes:
            break
        else:
            print("digite uma opçao valida\n")
    

    computador = random.choice(opcoes)
    print(f"voce escolheu {usuario} e o computador {computador} então :", end='')
    if usuario == computador:
        print(f"{amarelo}EMPATOU{finalizar}")
    elif jogo[usuario] == computador:
        print(f"{verde}VOCE GANHOU{finalizar}")
    else:
        print(f"{vermelho}COMPUTADOR GANHOU{finalizar}")

    print("\ndigite 1 para jogar novamente ou qualquer outro numero para encerrar o jogo\n")
    while True:
        try:
            num = int(input(""))
            break
        except:
            print("por favor apenas numeros!!!\n")
    if num != 1:
        break
        
