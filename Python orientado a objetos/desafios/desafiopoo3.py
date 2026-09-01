#crie uma classe chamada churrasco,informe quantas pessoas vão
#participar e mostre quanto de carne deve ser comprado. o custo total do churrasco e o custo por pessoas
        #consumo padrao é de 400g por pessoa
        #preço de 82,40/kg



class Churrasco:
    def __init__(self,nome_do_churrasco = '',pessoas = 0):
        self.nome = nome_do_churrasco
        self.pessoas = pessoas

    def analisar(self):

        consumo_do_churrasco = self.pessoas * 0.4

        preço_total = float(consumo_do_churrasco) * 82.40

        preço_por_convidado = float(preço_total/self.pessoas)

        return f'o custo total do {self.nome} sera de R${preço_total:,.2f}, equivalente a {consumo_do_churrasco:.2f}kg de carne, vai custar R${preço_por_convidado:,.2f} para cada pessoa'


sabado = Churrasco('churras dos cria',23)


print(sabado.analisar()) 