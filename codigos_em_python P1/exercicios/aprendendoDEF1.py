"""usando algoritmos simples de outras questoes do professor para aprender a definir funções"""


def descontar (valor_compra):
    if valor_compra >= 500:
        return valor_compra * 0.20
    elif valor_compra >= 200:
        return valor_compra * 0.10
    elif valor_compra >= 100:
        return valor_compra * 0.05
    else:
        return 0

while True:
    try:
        valor_compra = float(input("digite o valor da compra\n"))
        if valor_compra < 0:
            print("nao tem como fazer uma compra negativa\n")
            continue
        else:
            break
    except:
        print("por favor digite um valor valido")
    
valor_final = valor_compra - descontar(valor_compra)
print(f"Desconto: {descontar(valor_compra):.1f}R$")
print(f"Valor final : {valor_final}R$")