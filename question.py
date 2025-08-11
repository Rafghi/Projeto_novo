import os
import sys
from datetime import datetime

disp_st = 10
disp_pr = 5
disp_lu = 3
reservas = 0
maior_reservas = 0
nome_reserva_cara = ""
nome_tempo_maior = ""
maior_tempo = 0
menu = 1

while menu == 1:
    print("Digite 1 para fazer uma reserva")
    print("Digite 2 para sair")
    menu = int(input('Decida o que irá fazer: '))
    if menu == 2:
        sys.exit()
    nome = input("Qual o nome do respónsavel da reserva: ").strip()
    if nome == "":
        print("Nome inválido!")
        continue
    os.system("clear")

    formato = "%d/%m/%Y"
    check_in = input("Digite a data de Check-In (No modelo dd/mm/aaaa): ")
    check_in = datetime.strptime(check_in, formato).date()
    check_out = input("Digite a data de Check-Out (No modelo dd/mm/aaaa): ")
    check_out = datetime.strptime(check_out, formato).date()
    os.system('clear')
    if check_out < check_in:
        print("O Check-out não pode ser maior que o Check-in! Faça novamente")
        continue

    diárias = check_out - check_in

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

