import random
import time
jogo = [
' ',' ',' ',
' ',' ',' ',
' ',' ',' '
]

verde = '\033[1;32m'
end = '\033[m'
vermelho = '\033[1;31m'
amarelo = '\033[1;33m'
def vitorias():
    Listadevitorias = [
        [0 , 1 , 2], [3 , 4 , 5] , [6 , 7 , 8],
        [0 , 3 , 6] , [1 , 4 , 7], [2 , 5 , 8],
        [0 , 4 , 8]  , [2 , 4 , 6] 
    ]

    for linha in Listadevitorias:
        if jogo[linha[0]] == jogo[linha[1]] == jogo[linha[2]] and jogo[linha[0]] != ' ':
            if jogo[linha[0]] == 'O':
                print(f"{vermelho}o computador venceu{end}")
            else:
                print(f"{verde}o usuario venceu{end}")
            return True
    return False


def estrutura():
    texto1 = "escolha onde voce quer jogar,Digite a Letra Seguida do numero ex : [A1]"
    for linhas in texto1:
        print(linhas,end='',flush=True)
        
        time.sleep(0.02)
    print()

    
    print(f"{amarelo}             1      2      3{end}")
    print(f"\n\t{amarelo}A{end}    {jogo[0]}      {jogo[1]}      {jogo[2]} ")
    print(f"\n\t{amarelo}B{end}    {jogo[3]}      {jogo[4]}      {jogo[5]} ")
    print(f"\n\t{amarelo}C{end}    {jogo[6]}      {jogo[7]}      {jogo[8]} ")

def estrutura2():
    print(f"{amarelo}             1      2      3{end}")
    print(f"\n\t{amarelo}A{end}    {jogo[0]}      {jogo[1]}      {jogo[2]} ")
    print(f"\n\t{amarelo}B{end}    {jogo[3]}      {jogo[4]}      {jogo[5]} ")
    print(f"\n\t{amarelo}C{end}    {jogo[6]}      {jogo[7]}      {jogo[8]} ")


def empate():
    if ' ' not in jogo:
        print("DEU VELHA PARCEIRO")
        return True
    else:
        return False
 
valido = ['A1','A2','A3','B1','B2','B3','C1','C2','C3']
validopc = ['A1','A2','A3','B1','B2','B3','C1','C2','C3']
val = {
"A1" : 0,
'A2' : 1,
'A3' : 2,
'B1' : 3,
'B2' : 4,
'B3' : 5,
'C1' : 6,
'C2' : 7,
'C3' : 8,
}
titulo = 'Bem Vindo(a) Ao jogo da velha!!!!!'

for r in titulo:
    print(r,end='',flush=True)
    time.sleep(0.03)
print()

estrutura()
while True:
    while True:

        escolha_user = str(input("")).upper().strip()
        if escolha_user not in valido:
            print("Digite apenas valores Que Tenham no jogo")
            continue
        else:
           
            break
    if escolha_user in val and jogo[val[escolha_user]] != 'X' and jogo[val[escolha_user]] != 'O':

        jogo[val[escolha_user]] = 'X'
        validopc.remove(escolha_user)
    else:
        print("escolha invalida, Jogue apenas nos espaços vazios")
        continue

    if vitorias():
        estrutura2()
        break
    elif empate():
        break

    computador = random.choice(validopc)

    jogo[val[computador]] = 'O'
    validopc.remove(computador)

    
    if vitorias():
        estrutura2()
        break
    elif empate():
        break
        

    estrutura()

   