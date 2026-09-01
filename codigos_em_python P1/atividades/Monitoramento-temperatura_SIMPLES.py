print("\tbem vindo ao monitoramento da temperatira da nave!!\n")
temperatura = 0
soma = 0
media : float = 0
alertas = 0
contador = 0

while True:
    temperatura = float(input("qual a temperatura atual? digite [-1] PARA PARAR\n"))
    if temperatura == -1:
        break
    if temperatura < -1:
        print("valor invalido!!\n")
        continue
    
    elif (temperatura >=0 ) and (temperatura <= 40):
        soma = soma + temperatura
        media = media + 1
        print("Status atualizado = Normal\n")
    elif temperatura > 40:
        contador = contador + 1
        alertas = alertas + 1
        soma = soma + temperatura
        print("alerta [TEMPERATURA ALTA!!!!]\n")
media = (soma / contador)
print(f"um total de {alertas} registrados!!!\n")
print(f"a media da temperatura foi de {media:.2f}\n")
