
class Estabelecimento:
    def __init__(self,nome,cidade,quantidade,nicho):

        self.nome = nome
        self.cidade = cidade    
        self.quantidade = quantidade 
        self.nicho = nicho
        self.patrocinadores = []

    
    

    def aumentos (self,quantidade):
        self.quantidade += quantidade
        print(f'Quantidade atualizada para {self.quantidade}')

    def adionar_patrocinadores(self):
        funcionario = input("Digite o nome do patrocinador: ")
        if funcionario not in self.patrocinadores:
            
            self.patrocinadores.append(funcionario)

        else:
            
            print(f'Patrocinador ja esta na equipe {funcionario}')      


            
Supermercadosouza = Estabelecimento('souza_mercado','matureia-pb',1,'mercado')
mixmateus = Estabelecimento('mix_mateus','Patos-pb',4,'mercado')
postonossasenhora = Estabelecimento('posto_nossa_senhora','matureia-pb',1,'posto')
oficinaaladin = Estabelecimento('oficina_aladin','matureia-pb',3,'oficina')





'''area de testes '''
Supermercadosouza.adionar_patrocinadores()
postonossasenhora.adionar_patrocinadores()

print(Supermercadosouza.quantidade)
aumentos = Supermercadosouza.aumentos(100)

print(oficinaaladin.quantidade)

print(postonossasenhora.patrocinadores)

print(mixmateus.quantidade)

'''area de testes'''