while True:
    
    try:
        num = int(input("digite um numero\t"))
        if num < 0 :
            print("por favor digite um numero positivo\n")
            continue
        else:
            print(num)
            break
    except:
        print("digite um numero por favor")


num_texto = str(num)
novalista = []
voltas = len(num_texto)

for i in range(voltas - 1,-1,-1):
    novalista.append(num_texto[i])
print(f"{''.join(novalista)}")