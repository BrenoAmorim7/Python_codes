class Estabelecimento:
    def __init__(self, nome, cidade, quantidade, nicho):
        self.nome = nome
        self.cidade = cidade    
        self.quantidade = quantidade 
        self.nicho = nicho
        self.patrocinadores = [] 

    def aumentos(self, quantidade):
        self.quantidade += quantidade
        print(f'Quantidade atualizada para {self.quantidade}')

    def adicionar_patrocinador(self):
        while True:
            patrocinador = input(f"Digite o nome do patrocinador que voce quer adicionar ao {self.nome}: \n")

            if patrocinador not in self.patrocinadores:
                self.patrocinadores.append(patrocinador)
                print(f'Patrocinador {patrocinador} adicionado com sucesso ao {self.nome}!\n')
                break
            else:
                print(f'Patrocinador {patrocinador} já está na lista dos patrocinadores do {self.nome}.\n')

    def remover_patrocinador(self):
        while True:

            patrocinador = input(f"qual patrocinador do {self.nome} voce deseja remover???\n")
            if patrocinador in self.patrocinadores:
                self.patrocinadores.remove(patrocinador)
                break
            else:
                print(f"nao existe esse patrocinador no {self.nome}\n")
    
def listar_patrocinadores():
        print("escolha qual estabelecimento voce deseja listar os patrocinadores\n" 
        "[1] para supermercado_souza\n" 
        "[2] para mix_matheus\n" 
        "[3] para postonossa_senhora\n" 
        "[4] para oficina_aladin\n")
        escolha = int(input(""))

        if escolha == 1:
            print(Supermercadosouza.patrocinadores)
        elif escolha == 2:
            print(mixmateus.patrocinadores)
        elif escolha == 3:
            print(postonossasenhora.patrocinadores)
        elif escolha == 4:
            print(oficinaaladin.patrocinadores)
        else:
            print('escolha inexistente')
    


Supermercadosouza = Estabelecimento('souza_mercado', 'matureia-pb', 1, 'mercado')
mixmateus = Estabelecimento('mix_mateus', 'Patos-pb', 4, 'mercado')
postonossasenhora = Estabelecimento('posto_nossa_senhora', 'matureia-pb', 1, 'posto')
oficinaaladin = Estabelecimento('oficina_aladin', 'matureia-pb', 3, 'oficina')


    
Supermercadosouza.adicionar_patrocinador()  
Supermercadosouza.adicionar_patrocinador()

oficinaaladin.adicionar_patrocinador()

oficinaaladin.adicionar_patrocinador()
print(oficinaaladin.patrocinadores)
print(Supermercadosouza.patrocinadores)


oficinaaladin.remover_patrocinador()
Supermercadosouza.remover_patrocinador()

print(Supermercadosouza.quantidade)
Supermercadosouza.aumentos(100)

print(oficinaaladin.quantidade)

print(oficinaaladin.patrocinadores)
print(Supermercadosouza.patrocinadores)

print(mixmateus.quantidade)


listar_patrocinadores()