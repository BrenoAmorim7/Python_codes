#questão 1 . implementar pseudocodigo em python
"""usando algoritmos simples de outras questoes do professor para aprender a definir funções"""
def classificar (idade):
    if idade < 16:
        return "candidato nao elegivel : idade minima nao atingida"
    elif media >= 9 and renda <= 2000:
        return "bolsa integral"
    elif media >= 8 and renda <= 3500:
        return "bolsa de 50%"
    elif media >= 7 and renda <= 5000:
        return "bolsa de 25%"
    else:
        return "nao aprovado para bolsa"

nome = str(input("digite o nome do candidato\n"))
idade = int(input("digite a idade do candidato\n"))
media = float(input("digite a media final do candidato\n"))
renda = float(input("digite a renda familiar mensal do candidato\n"))


print(f"{classificar(idade)}")