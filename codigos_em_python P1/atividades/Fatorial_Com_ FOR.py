teste = True


while True:
    num = int(input("digite qual numero voce quer o fatorial!: \n"))


    resultado = 1

    for contador in range (1,num+1, 1):
        novoresultado = resultado * contador
    
        print(f"{contador} * {resultado} = {novoresultado}")
        resultado = novoresultado

    print(f"{resultado}")
    while teste:
        try:
            escolha = int (input("digite [1] para fazer com outro numero e [0] para encerrar o programa\n"))
            break
        except:
            print("por favor digite um numero inteiro\n")
    if escolha == 1:
        continue
    elif (escolha != 1) and (escolha == 0):
        break
    
    else:
        print("numero invalido! programa encerrado")
        break