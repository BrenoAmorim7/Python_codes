

while True:
    try:
        n = int(input("digite a quantidade de linhas que a matriz vai ter\t"))
        c = int(input("digite a quantidade de colunas que a matriz vai ter\t"))
        break
    except:
        print("por favor digite numeros inteiros!!!!\n")
        continue


for linhas in range(n):
    for coluna in range(c):
    
        print("x " ,end= '')
    
    print()