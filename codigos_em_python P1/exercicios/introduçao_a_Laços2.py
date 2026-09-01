
login = input("digite seu usuario de login\n")
senha = input("digite sua senha\n")

while login == senha:
    print("usuario e senha nao podem ser iguais \n")
    senha = input("digite novamente uma outra senha\n")

print( "\tseu login e senha sao respectivamente\n")
print("login    senha")
print(f"  {login}       {senha}")