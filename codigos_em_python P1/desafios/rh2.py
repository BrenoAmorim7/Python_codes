dados = [
   ['TI','breno nunes',10000,'111.111.111-11','14/02/2007'],
   ['TI','joao',1000,'111.111.111-14','10/05/2222'],
   ['RH','maria',5200,'111.111.111-22','29/03/2222'],
   ['RH','pedro',6000,'111.111.111-25','5/05/2222'],
   ['GESTAO','murilo',4780,'111.111.111-40','12/09/2222'],
   ['GESTAO','otavio',4500,'111.111.111-50','23/11/2222']
]
departamentos = ['TI','FINANCEIRO','RH','GESTAO']
pergunta = ['MENU','PARAR']


def cpfvalido(cpf):
    if len(cpf) != 14:
        return False

    if cpf[3] != '.' or cpf[7] != '.' or cpf[11] != '-':
        return False
    else:
        return True

def olhardata(data):
    
    
    if len(data) != 10:
        return False

    if data[2] != '/' or data[5] != '/':
        return False
    
    return True

def cpfrepitido(cpf):
    for j in range(len(dados)):
                if cpf == dados[j][3]:
                    print("esse cpf ja esta cadastrado por favor insira um cpf valido!!!\n")
                    return False
    return True            

def adicionar():

    print("adionando outro usuario\n")
    while True:

        departamento = input('qual departamento? [TI],[FINANCEIRO],[RH],[GESTAO] \t ').upper().strip()
        if departamento != 'TI' and departamento != 'RH' and departamento != 'GESTAO' and departamento != 'FINANCEIRO':
            continue
        else:
            break

    while True:

        nome = input("digite o nome do funcionario\n")
        
        if len(nome) < 2 or len(nome) > 100:
            continue
        else:
            if nome.isalpha():
                break
            else:
                continue

    while True:
        cpf = input("digite o cpf do funcionario nesse formato!!! [xxx.xxx.xxx-xx]")
        cpfvalido(cpf)
        if cpfvalido(cpf) == False:
            continue
        else:
            if not cpfrepitido(cpf):
                continue
            else:
                break
    while True:
        data = input("digite a data de nascimento do funcionario no formato --> XX/XX/XXXX <---")
        try:
            dia = int(data[:2])
            mes = int(data[3:5])
            ano = int(data[6:10])
            mes30 = [4,6,9,11]
            mes31 = [1,3,5,7,8,10,12]
            mes28 = [2]
            if mes > 12 or mes < 1:
                print("so existem 12 meses")
                continue
            if mes in mes31:
                if dia > 31 or dia < 1:
                    print("esse mes so tem 31 dias")
                    continue
            elif mes in mes30:
                if dia > 30 or dia < 1:
                    print("esse mes so tem 30 dias")
                    continue
            elif mes in mes28:
                if dia > 28 or dia < 1:
                    print("esse mes so tem 28 dias , ou 29 em anos bissextos")
                    continue
            
            
            
            
            break
        except:
            continue

    while True:
        try:
            salario = float(input("digite o salario que o funcionario recebe\t"))

            if salario < 0 :
                print("salario invalido, por favor digite um val9r valido")
                continue
            else:
                break
        except:
            continue

    new = []
    new.append(departamento)
    new.append(nome)
    new.append(salario)
    new.append(cpf)
    new.append(data)
    
    dados.append(new)
    print(new)

def procurar():
    pessoa = input("digite o nome ou cpf da pessoa que voce deseja procurar\t")

    for i in range(len(dados)):
        if dados[i][1] == pessoa:
            print(dados[i])
        
        if dados[i][3] == pessoa:
            print(dados[i])

def procurarderp():
    while True:

        departamento_procura = input("escolha um departamento [RH]-[TI]-[FINANCEIRO]-[GESTAO]\t").strip().upper()

        if departamento_procura not in departamentos:
            print("por favor digite apenas uma das opçoes validas:", end='')
            print(*departamentos)
        else:
            break
    for i in range (len(dados)):
        if dados[i][0] == departamento_procura:
            print(*dados[i])

def remover():
        remove = input("digite o cpf do funcionario que voce quer remover ex : XXX.XXX.XXX-XX\t")
        if len(remove) != 14:
            return False
        if remove[3] != '.' or remove[7] != '.' or remove[11] != '-' :
            print("erro!! digitaçao invalida")
            return False

        encontrado = False

        for i in range(len(dados)):
            if remove == dados[i][3]:
                print(f"usuario removido --> ",end='')
                print(*dados[i])
                del dados[i]
                encontrado = True
                break
                    
        if not encontrado:
            print("nao tem nenhum funcionario cadastrado com esse cpf\n")
            return False
                 
while True:
    def menu():
        print('-' * 40)
        print("[1] adicionar novo funcionario ")
        print("[2] exibir funcionario especifico por nome ou cpf")
        print("[3] mostrar listas de funcionarios por departamento ")
        print("[4] para alterar ou remover um funcionario por cpf")
        print('-' * 40)
    menu()
    while True:
        try:

            escolha = int(input("digite aq a sua escolha\t"))
            if escolha < 1 or escolha > 4:
                print("nao tem essa opçao!!!!\n")
                continue
            else:
                break
        except:
            print("nao tem essa opçao!!!!\n")
            continue   
    if escolha == 1:
        adicionar() 

    elif escolha == 2:
        procurar()

    elif escolha == 3:
        procurarderp()

    elif escolha == 4:
        while remover():

            remover()
    
    print("\ndigite [menu] para voltar para o menu")
    print("digite [parar] para encerrar o programa\n")

    while True:
        escolhafinal = input("  ").strip().upper()

        if escolhafinal not in pergunta:
            print("por favor digite uma opçao valida")
            continue
        else:
            break
    if escolhafinal == pergunta[0]:
        continue
    else:
        break
