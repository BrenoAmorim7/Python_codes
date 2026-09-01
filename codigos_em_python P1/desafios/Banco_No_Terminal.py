print("bem vindo ao seu novo banco\n")
valoratual = 0
print(f"CONTA NOVA o seu saldo é de {valoratual} reais\n")


def depositar(valordeposito,valoratual):
    
    return valordeposito + valoratual

def sacar (valoratual,valorsaque):

    return valoratual - valorsaque
while True:
    print("\033[41m bem vindo ao seu banco pessoal\033[m\n")
    print("digite \033[1;33;40m[1]\033[m para \033[1;33;40mDEPOSITAR\033[m na sua conta")
    print("digite \033[1;32;40m[2]\033[m para o \033[1;32;40mSALDO\033[m da sua conta")
    print("digite \033[1;36;40m[3]\033[m para \033[1;36;40mSACAR\033[m")
    print("digite \033[1;35;40m[4]\033[m para fazer um \033[1;35;40mPIX\033[m")
    print("digite \033[1;37;40m[5]\033[m  para acessar nossa \033[1;37;40mLOJA VIRTUAL\033[m\n ")
    print("digite \033[1;31;40m[0]\033[m para \033[1;31;40mENCERRAR\033[m o programa")
    escolha = int(input("\n"))

    if escolha == 1:
        while True:
            valordeposito = float(input("digite a quantidade que voce quer depositar\n"))
            valoratual = depositar(valordeposito,valoratual)
            print("ditgite [1] para depositar mais dinheiro\n")
            print("digite [2] para voltar ao painel inicial\n")
            escolha2 = int(input(""))
            if escolha2 == 1:
                continue
            else:
                break
    elif escolha == 2:
        print(f"voce tem exatos {valoratual} R$ na sua conta\n")
    elif escolha == 3:
        while True:
            valorsaque = float(input("diga quanto voce quer sacar\n"))
            if valorsaque <= valoratual:
                valoratual = sacar(valoratual,valorsaque)
                print(f"voce sacou {valorsaque}R$, e ficou com {valoratual} R$ na conta")
                print("digite [1] para encerrar o saque e voltar a tela inicial\n")
                print("digite [2] para sacar dinheiro de novo")
                escolha2 = int(input("" ""))
                if escolha == 1:
                    break
                else:
                    continue
            else:
                print("valor invalido voce nao tem saldo suficiente!!!\n")
                print("digite [1] para tentar sacar de novo\n")
                print("digite [2] para voltar a tela inicial do programa\n")
                escolha2 = int(input("" ""))
                if escolha2 == 1:
                    continue
                else:
                    break
    elif escolha == 4:
        while True:
            print("bem vindo a area pix\n")
            chave = int(input("digite a chave pix\n"))
            valorpix = float(input("quanto voce quer transferir?\n"))
            if valorpix > valoratual:
                print("\033[1;31mvoce nao tem saldo suficiente\033[m\n")
                break
            else:
                valoratual -= valorpix
                print(f"pix no valor de {valorpix} para a {chave}\n")
                print("digite \033[1;33m[1] \033[m para voltar a area de pix\n")
                print("digite \033[1;33m[2] \033[m para voltar ao painel inicial\n")
                escolha2 = int(input(""))
                if escolha2 == 1:
                    continue
                else:
                    break


    else:
        break
print("obrigado por usar nosso serviço, VOLTE SEMPRE!!!!!")
