class Pcgamer:

    def __init__(self):
        self.nome = '?'
        self.memoria_ram = 0
        self.processador = '?'
        self.placa_de_video = '?'


    def mensagem(self):
        return f'o processador do {self.nome} é um {self.processador}, ele tem {self.memoria_ram} Gigabytes de memoria e tem uma {self.placa_de_video} de placa de video\n '



pc_da_faculdade = Pcgamer()
pc_da_faculdade.nome = 'Pc_do_lab'
pc_da_faculdade.memoria_ram = 8
pc_da_faculdade.processador = 'Ryzen 7'
pc_da_faculdade.placa_de_video = 'gtx 550'

pc_de_casa = Pcgamer()

pc_de_casa.nome = 'pc_gamer_branco'
pc_de_casa.memoria_ram = 16
pc_de_casa.processador = 'intel i5'
pc_de_casa.placa_de_video = 'Rx 580'

print(pc_da_faculdade.mensagem())
print(pc_de_casa.mensagem())