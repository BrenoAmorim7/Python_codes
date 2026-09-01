class Livro:
    
    def __init__(self,nome_do_livro = '',quantidade_de_paginas = 0):
        self.nome = nome_do_livro
        self.paginas = quantidade_de_paginas
        self.pagina_atual = 1

    def avancar_paginas(self):
        if self.pagina_atual >= self.paginas:
                    print(f"Você já concluiu a leitura do livro '{self.nome}'!")
                    return
        print(f'bem vindo ao livro {self.nome} voce esta na pagina {self.pagina_atual}')

        avancar = int(input("quantas paginas deseja avançar?\n"))
        
        if self.pagina_atual <= self.paginas:

            destino = self.pagina_atual + avancar
            pagina_inicial = self.pagina_atual

            estourou = destino > self.paginas
            if estourou:
                destino = self.paginas + 1

            for i in range(self.pagina_atual,destino ):
                print(f" pag  {self.pagina_atual} ->> ",end='')
                self.pagina_atual+= 1

            if estourou:

                tentativa = self.paginas - pagina_inicial
                print(f"\n\033[1;34mvoce pediu pra passar {avancar} paginas, mas com apenas {tentativa} voce chegou ao final do livro!!\033[m")
                
            elif self.pagina_atual == self.paginas:
                 print(f"parabens voce chegou na pag {self.pagina_atual},voce terminou o livro!!!!")

livro1 = Livro('biblia sagrada',100)

livro1.avancar_paginas()

livro1.avancar_paginas()

