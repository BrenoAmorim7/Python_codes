class Pcgamer:

    def __init__(self, nome = 'vazio ',memoria_ram = 0,processador = 'vazio',placa_de_video = 'vazio'):

        self.nome = nome
        self.memoria_ram = memoria_ram
        self.processador = processador
        self.placa_de_video = placa_de_video

      
    def __str__(self):
        return f'o processador do {self.nome} é um {self.processador}, ele tem {self.memoria_ram} Gigabytes de memoria e tem uma {self.placa_de_video} de placa de video\n '


pc_da_faculdade = Pcgamer('pc_do_lab',8,'ryzen 5','gtx 550 ti')



pc_de_casa = Pcgamer(input('digite o nome: '),int(input("quantos gb de memoria ram? ")),input("qual processador ele usa? "),input("qual placa de video ele usa? "))



print(pc_da_faculdade)
print(pc_de_casa)