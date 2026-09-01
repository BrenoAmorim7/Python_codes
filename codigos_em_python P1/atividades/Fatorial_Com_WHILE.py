contador = 1 
resultado = 1

num = int(input("voce quer saber o fatorial de qual numero? \n"))


while contador <= num:   #EXEMPLO : NUM = 4
    novoresultado = resultado * contador
    print(f"{contador} x {resultado} = {novoresultado}")
    resultado *= contador
    contador += 1
    
    
print(f"o fatorial do numero {num} é = {resultado}")

# A LOGICA POR TRAS É A SEGUINTE

#1 * 1       PRIMEIRO LOOP
#1 * 2       SEGUNDO LOOP
#2 * 3       TERCEIRO LOOP
#6 * 4 = 24      ULTIMO LOOP RESULTADO

#Coloquei os '#' explicando o codigo para auxiliar um colega da turma a entender a logica por tras