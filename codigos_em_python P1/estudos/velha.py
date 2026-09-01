import random
jogo = [
' ',' ',' ',
' ',' ',' ',
' ',' ',' '
]

verde = '\033[1;32m'
end = '\033[m'
def estrutura():
    print("escolha onde voce quer jogar,Digite a Letra Seguida do numero ex : [A1] \n")
    print("             1      2      3")
    print(f"\n\tA    {jogo[0]}      {jogo[1]}      {jogo[2]} ")
    print(f"\n\tB    {jogo[3]}      {jogo[4]}      {jogo[5]} ")
    print(f"\n\tC    {jogo[6]}      {jogo[7]}      {jogo[8]} ")

def estrutura2():
    print("             1      2      3")
    print(f"\n\tA    {jogo[0]}      {jogo[1]}      {jogo[2]} ")
    print(f"\n\tB    {jogo[3]}      {jogo[4]}      {jogo[5]} ")
    print(f"\n\tC    {jogo[6]}      {jogo[7]}      {jogo[8]} ")

def vitoria1():
    if jogo[0] == jogo[1] and jogo[0] == jogo[2] and jogo[0] != ' ':
        if jogo[0] == 'O':
            print("computador venceu\n")
            return True
        elif jogo[0] == 'X':
            print(f"{verde}USUARIO VENCEU{end}\n")
            return True
        else:
            return False
def vitoria2():
    if jogo[3] == jogo[4] and jogo[3] == jogo[5] and jogo[3] != ' ':
        if jogo[3] == 'O':
            print("o computador venceu ")
            return True
        elif jogo[3] == 'X':
            print(f"{verde}USUARIO VENCEU{end}\n")
            return True
        else:
            return False
def vitoria3():
    if jogo[6] == jogo[7] and jogo[6] == jogo[8] and jogo[6] != ' ':
        if jogo[6] == 'O':
            print("o computador venceu ")
            return True
        elif jogo[6] == 'X':
            print(f"{verde}USUARIO VENCEU{end}\n")
            return True
        else:
            return False    
def vitoria4():
    if jogo[0] == jogo[3] and jogo[0] == jogo[6] and jogo[0] != ' ':
        if jogo[0] == 'O':
            print("o computador venceu ")
            return True
        elif jogo[0] == 'X':
            print(f"{verde}USUARIO VENCEU{end}\n")
            return True
        else:
            return False
def vitoria5():
    if jogo[1] == jogo[4] and jogo[1] == jogo[7] and jogo[1] != ' ':
        if jogo[1] == 'O':
            print("o computador venceu ")
            return True
        elif jogo[1] == 'X':
            print(f"{verde}USUARIO VENCEU{end}\n")
            return True
        else:
            return False     
def vitoria6():
    if jogo[2] == jogo[5] and jogo[2] == jogo[8] and jogo[2] != ' ':
        if jogo[2] == 'O':
            print("o computador venceu ")
            return True
        elif jogo[2] == 'X':
            print(f"{verde}USUARIO VENCEU{end}\n")
            return True
        else:
            return False
def vitoria7():
    if jogo[0] == jogo[4] and jogo[0] == jogo[8] and jogo[0] != ' ':
        if jogo[0] == 'O':
            print("o computador venceu ")
            return True
        elif jogo[0] == 'X':
            print(f"{verde}USUARIO VENCEU{end}\n")
            return True
        else:
            return False   
def vitoria8():
    if jogo[2] == jogo[4] and jogo[2] == jogo[6] and jogo[2] != ' ':
        if jogo[2] == 'O':
            print("o computador venceu ")
            return True
        elif jogo[2] == 'X':
            print(f"{verde}USUARIO VENCEU{end}\n")
            return True
        else:
            return False
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
print("bem vindo ao jogo da velha\n")

print("escolha onde voce quer jogar,Digite a Letra Seguida do numero ex : [A1] \n")
print("             1     2     3")
print(f"\n\tA   {jogo[0]}    {jogo[1]}    {jogo[2]} ")
print(f"\n\tB   {jogo[3]}    {jogo[4]}    {jogo[5]} ")
print(f"\n\tC   {jogo[6]}    {jogo[7]}    {jogo[8]} ")
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
    if vitoria1():
        estrutura2()
        break
    elif vitoria2():
        estrutura2()
        break
    elif vitoria3():
        estrutura2()
        break
    elif vitoria4():
        estrutura2()
        break
    elif vitoria5():
        estrutura2()
        break
    elif vitoria6():
        estrutura2()
        break
    elif vitoria7():
        estrutura2()
        break
    elif vitoria8():
        estrutura2()
        break
    elif empate():
        break
    computador = random.choice(validopc)

    jogo[val[computador]] = 'O'
    validopc.remove(computador)

    if vitoria1():
        estrutura2()
        break
    elif vitoria2():
        estrutura2()
        break
    elif vitoria3():
        estrutura2()
        break
    elif vitoria4():
        estrutura2()
        break
    elif vitoria5():
        estrutura2()
        break
    elif vitoria6():
        estrutura2()
        break
    elif vitoria7():
        estrutura2()
        break
    elif vitoria8():
        estrutura2()
        break
    elif empate():
        break
    estrutura()

   