entrada = " "
while len(entrada) != 6:
    entrada = input ("digite 6 valores separados por um espaço " " cada um\n").split()
    if len(entrada) == 6:
        n1,n2,n3,n4,n5,n6 = map(float, entrada)
        print(f" {n1} {n2} {n3} {n4} {n5} {n6}")
    else:
    
        print(f"eu pedi 6 valores, voce digitou {len(entrada)} numeros\n")
        print("digite novamente\n")
        entrada = input ("digite 6 valores separados por um espaço " " cada um\n").split()
        continue