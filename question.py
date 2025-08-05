# ENTREGA 1:

import sys
from datetime import datetime

# NOME:

nome = input("Digite o nome do responsável pela reserva: ").strip()
 
if nome == "":
    print("Nome inválido! Nome vazio!")
    sys.exit()

# DATA:

formato = "%d/%m/%Y"

check_in = input("Digite a data de Check-In (No modelo dd/mm/aaaa): ")
check_in = datetime.strptime(check_in, formato).date()

check_out = input("Digite a data de Check-Out (No modelo dd/mm/aaaa): ")
check_out = datetime.strptime(check_out, formato).date()

if check_out < check_in:
    print("O Check-out não pode ser maior que o Check-in! Faça novamente")
    sys.exit()

diárias = check_out - check_in

# TIPO DE QUARTO:

quarto = input("Digite o tipo de quarto desejado (Standard, Premium ou Luxo): ")

if quarto == "Standard" or "standard":
    diaria = int(100)
elif quarto == "Premium" or "premium":
    diaria = int(180)
elif quarto == "Luxo" or "luxo":
    diaria = int(250)
else:
    print("Este quarto não existe!")
    sys.exit()

preço = diaria * diárias.days

print(f"Olá {nome}! Seu Check-in está marcado para o dia {check_in} e seu Check-out está marcado para o dia {check_out}. Ao total, você ficará {diárias.days} dias conosco! Você ficará no quarto {quarto}. Ao total, o preço será R${preço}.")
