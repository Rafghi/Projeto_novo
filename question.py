import sys
from datetime import datetime

# NOME:

nome = input("Digite o nome do responsável pela reserva: ").strip()
 
if nome == "":
    print("Nome inválido! Nome vazio!")
    sys.exit()

# DATA:

formato = "%d/%m/%Y"

data = input("Digite a data de Check-In (No modelo dd/mm/aaaa): ")
data = datetime.strptime(data, formato).date()

data2 = input("Digite a data de Check-Out (No modelo dd/mm/aaaa): ")
data2 = datetime.strptime(data2, formato).date()

diferença = data - data2

print(data)
print(data2)
print(diferença.days)

# TIPO DE QUARTO:

quarto = input("Digite o tipo de quarto desejado (Standard, Premium ou Luxo): ")

if quarto == "Standard":
    diaria = int(100)
elif quarto == "Premium":
    diaria = int(180)
elif quarto == "Luxo":
    diaria = int(250)
