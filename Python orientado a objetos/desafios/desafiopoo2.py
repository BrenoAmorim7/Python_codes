#crie uma classe chamada pruduto, onde podemos cadastrar nome e o preço.crie tambem 
#um metodo que mostre uma etiqueta de preço do produto
 
class Produto:
    def __init__(self,nome = '',preço = 0):
        self.nome = nome
        self.preço = preço



    def estiqueta(self):
        return f'{self.nome} | R$ {self.preço:,.2f}'



mouse = Produto('mouse',5)

teclado = Produto('teclado semi mecanico rgb',30)


print(mouse.estiqueta())

print(teclado.estiqueta())

