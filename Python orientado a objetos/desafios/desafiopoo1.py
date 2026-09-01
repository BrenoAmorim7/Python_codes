#crie uma classe chamada funcionario, onde podemos cadastrar nome,setor e cargo. crie tambem
#um metodo que permita ao funcionario se apresentar

class Funcionario:
    def __init__(self, nome = '',setor = '',cargo = ''):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo


    def apresentaçao(self):
        return f'oi meu nome é {self.nome} trabalho no setor de {self.setor} no cargo de {self.cargo}'



joao = Funcionario('joao','ti','suporte de ti')








print(joao.apresentaçao())
        