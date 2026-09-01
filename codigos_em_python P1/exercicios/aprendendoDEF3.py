"""usando algoritmos simples de outras questoes do professor para aprender a definir funções"""
def classificar(idade):
    if idade < 12:
        return "infantil"
    elif idade <= 14:
        return "juvenil"
    elif idade <= 17:
        return "junior"
    else:
        return "adulto"
    
categorias = {
    "infantil" : 0,
    "juvenil" : 0,
    "junior" : 0,
    "adulto" : 0
}
aluno = 0    
for i in range(10):
    aluno += 1
    print(f"\033[1;33mAluno {aluno}\033[m")
    while True:                                                    
            nome = str(input("digite o nome do aluno\t"))
            if not nome.isalpha():                                      
                print("digite um nome valido por favor meu amigo\n")
                continue
            else:
                break

    while True:
        try:
            idade = int(input("digite a idade do aluno\t"))
            if idade < 0:
                print("idade invalida\n")    
            else:
                break
        except:
            print("digite uma idade valida\n")

    categoria = classificar(idade)

    categorias[categoria] +=1

print(f"{categorias['infantil']} alunos infantis")    
print(f"{categorias['juvenil']} alunos juvenis")   
print(f"{categorias['junior']} alunos junior")   
print(f"{categorias['adulto']} alunos adultos")   

