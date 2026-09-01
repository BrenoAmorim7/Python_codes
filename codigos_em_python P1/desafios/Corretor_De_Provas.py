f = 1
alunos = int(0)
maior = 0
menor = 100
media = 0
loopgeral = True
questao = 1
looplista1 = True
looplista2 = True
print("professor digite o gabarito das 10 questoes da prova aqui!! apenjas separados por espaço\n")
while looplista1 :
    
        gabarito = input(" ").upper().split()
        if not all(item.isalpha() for item in gabarito):
            print("Erro: Por favor, digite apenas letras!!!")
            looplista1 = True
        if len(gabarito) < 10:
            print(f"por favor digite o gabarito das 10 QUESTOES voce digitou apenas de {len(gabarito)} questoes")
            looplista1 = True
        elif len(gabarito) > 10:
            print(f"por favor digite o gabarito apenas das 10, voce digitou de {len(gabarito)} questoes")
            looplista1 = True
        else:
            looplista1 = False

while loopgeral:
    while looplista2:

            resposta = input("digite todas as respostas que o aluno marcou na sua prova separada por espaços\n").upper().split()
            if not all(item.isalpha() for item in resposta):
                print("por favor digite apenas letras!!!!!!!!!")
                looplista2 = True
            if len(resposta) < 10:
                print(f"por favor digite as 10 respostas voce digitou apenas {resposta} \n")
            elif len(resposta) > 10:
                print(f"por favor digite apenas 10 respostas, voce digitou {resposta}\n")
            else:
                looplista2 = False
    j = 0
    acertos = 0
    nota = 0
    for i in range (1,11):
        if resposta[j] == gabarito[j]:
            print(f"voce \033[1;32macertou\033[m a questao {questao} o gabarito era {gabarito[j]}\n")
            acertos += 1
        else:
            print(f"voce \033[1;31merrou\033[m a questao {questao} voce marcou {resposta[j]} e a resposta certa era {gabarito[j]}\n")
        j += 1
        questao += 1

    if acertos >= maior :
        maior = acertos
    if acertos <= menor :
        menor = acertos
    alunos +=1
    media += acertos
    print("Para continuar com as respostas de outro aluno digite \033[1;33m[1]\033[m\n")
    print("para encerrar o programa e ver os resultados digite \033[1;33m[0]\033[m\n")
    while True:
        try:
            escolha = int(input("->\n"))           
            if escolha == 1:
                break
            elif escolha == 0:
                loopgeral = False
                break
            else:
                print("dite apenas os valores [0] ou [1]\n")
        except:
            print("por favor digite apenas os numeros INTEIROS [1] ou [0]\n")

media = media / alunos
print(f"O maior numero de acertos foi {maior} e o menor foi {menor}")
print(f"Exatamente {alunos} alunos usaram o sistema ")
print(f"A media de todas as notas foi de {media}")
