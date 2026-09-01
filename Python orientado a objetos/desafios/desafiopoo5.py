#crie a classe Gamer, onde podemos cadastrar nome,nick e jogos
#favoritos de uma pessoa. crie tambem um metodo que permita mostrar a ficha desse gamer

azul = '\033[1;32m'
amarelo = '\033[1;33m'
fim = '\033[m'
class Gamer:
    def __init__ (self,nome = '',nick = '',jogos_favoritos = []):
        self.nome = nome
        self.nick = nick
        self.jogos_favoritos = jogos_favoritos

    def add_favoritos (self):
        jogo = input(f"bem vindo {self.nome} qual jogo voce quer adicionar aos seus favoritos?\n")

        if jogo not in self.jogos_favoritos:
            self.jogos_favoritos.append(jogo)
        else:
            print("esse jogo ja foi adicionado a sua lista de favoritos")
            escolha = int(input("digite 1 para adiconar outro jogo ou 0 para encerrar!!!!\n"))
            if escolha == 1:
                self.add_favoritos()
            else:
                return

    def ficha (self):
        self.jogos_favoritos.sort()
        print(f"\n{amarelo}nome:{fim}{self.nome} - {amarelo}nick:{fim}{self.nick}")
        print(f"{azul}lista de jogos favoritos:{fim} ",end="")
        print(" - ".join(self.jogos_favoritos))


breno = Gamer('breno nunes','breno_199',)

breno.add_favoritos()
breno.add_favoritos()
breno.add_favoritos()

breno.ficha()


