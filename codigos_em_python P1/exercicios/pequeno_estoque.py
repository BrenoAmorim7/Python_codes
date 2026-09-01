print("\tbem vindo a loja de maçã\n ")

maca = 25 #aqui eu defini o estoque
preco = 0
preco1 = 1.50
preco2 = 1.20
total = 0
vendidos = 0
while (maca > 0) :
    print(f"temos exatamente {maca} maçãs em estoque\n") 
    pedido =float(input("digite quantas maças voce quer comprar\n")) # aqui armazena o pedido

    if pedido == 0: # se pedido for igual a zero macas o loop para
        break 
    if pedido > maca:
        print(f"desculpe , estoque insuficiente temos apenas {maca} unidades\n")
        continue #continue serve para voltar pro comeco do loop
    if pedido < 6:
        preco  = preco1
    else:
        preco = preco2
    vendidos = vendidos + pedido
    valordevenda = pedido * preco 
    total += valordevenda
    maca -= pedido
   
    print(f"Você comprou {pedido} maçãs por R$ {valordevenda:.2f}. Restam {maca} no estoque.\n")
if maca == 0:
    print ("expediente encerrado\n")

print(f"\tvoce comprou um total de {vendidos} macas por {total} reais\n")




 