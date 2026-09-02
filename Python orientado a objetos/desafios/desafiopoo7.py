#crie a classe Caneta, que simule o funcionamento de uma caneta colorida, podendo escrever frases na cor reativa,
#a caneta so podera escrever se estiver destampada!!!



lista_de_textos = []
azul ='\033[1;34m'
verde = '\033[1;32m'
amarelo = '\033[1;33m'
final = '\033[m'


class Caneta:
    def __init__ (self,nome,cor,tampa):
        self.nome = nome
        self.cor = cor
        self.tampa = tampa

    def tampa_caneta(self):
        print(f"a {self.cor}{self.nome}{final} esta atualmente {self.tampa}!!!!")
        if self.tampa == 'tampado':

        
            print("digite 1 para manter a caneta tampada")
            print("digite 2 para destampar a caneta")
            opçao1 = int(input(""))


            if opçao1 == 1 and self.tampa == 'tampado':
                print("a caneta ja esta tampada!!!!!")
            elif opçao1 == 1 and self.tampa == 'destampado':
                self.tampa = 'tampado'
            elif opçao1 == 2 and self.tampa == 'tampado':
                self.tampa = 'destampado'
            elif opçao1 == 2 and self.tampa == 'destampado':
                print("a caneta ja esta destampada!!!!!")
        
    def escrever(self):
        self.tampa_caneta()
        if self.tampa == 'tampado':
            print("voce nao conseguira escrever com a tampa da caneta tampada!!!!")
            return

        escolha = input("digite o texto que voce quer escrever:   ")
        var = f'\n{self.cor}{escolha}{final}'
       
        lista_de_textos.append(var)
        

caneta1 = Caneta('Caneta_azul',azul,'tampado')
caneta2 = Caneta('Caneta_verde',verde,'destampado')
caneta3 = Caneta('Caneta_amarela',amarelo,'tampado')


caneta1.escrever()  
caneta2.escrever()
caneta3.escrever()


print(*lista_de_textos)