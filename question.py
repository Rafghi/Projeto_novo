import os
import sys
from datetime import datetime

disp_st = 10
disp_pr = 5
disp_lu = 3
reservas = 0
total_reservas = 0
maior_reservas = 0
nome_reserva_cara = ""
nome_tempo_maior = ""
maior_tempo = 0
menu = 1

while menu == 1:
    os.system("clear")
    print("Digite 1 para fazer uma reserva")
    print("Digite 2 para sair")
    print("...................")
    menu = int(input('Decida o que irá fazer: '))
    if menu == 2:
        sys.exit()
    print("")
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

    tempo_dias = check_out - check_in
    Quantida_de_dias = tempo_dias.days

    if Quantida_de_dias > maior_tempo:
        maior_tempo = Quantida_de_dias
        nome_maior_tempo = nome

    if Quantida_de_dias < 0:
        print("Data de check-in maior que de check-out")
        continue
    os.system("clear")

    if check_out < check_in:
        print("O Check-out não pode ser maior que o Check-in! Faça novamente")
        continue

    diárias = check_out - check_in

    print("Abaixo, estarão listados os quartos disponíveis")
    print(".............")
    print("Quarto Standard = ",disp_st)
    print("Quarto Premium = " ,disp_pr)
    print("Quarto Luxo = ",disp_lu)
    print(".............")

    quarto = int(input("""Qual o tipo de quarto: 
    Digite 1 para Standard 
    Digite 2 para Premuim 
    Digite 3 para Luxo 
                       
    Quarto escolhido: """))
    os.system("clear")

    if quarto == 1:
        quantidade_quartos = int(input('Qual a quantidade de quartos standard você quer: '))
        disp_st -= quantidade_quartos
        if disp_st < 0:
            print('Não temos essa quantidade de quantos disponíveis para esse quarto')
        else:
            if quantidade_quartos > maior_reservas:
                maior_reservas = quantidade_quartos
                nome_reserva_mais_cara = nome
            valor_dias = tempo_dias * 100
            total_reservas += valor_dias
    
    
    elif quarto == 2:
        quantidade_quartos = int(input('Qual a quantidade de quartos premium você quer: '))
        disp_pr -= quantidade_quartos
        if disp_st < 0:
            print('Não temos essa quantidade de quantos disponíveis para esse quarto')
        else:
            if quantidade_quartos > maior_quant_reserva:
                maior_quant_reserva = quantidade_quartos
                nome_reserva_mais_cara = nome
            valor_dias = Quantida_de_dias * 180
            total_reservas += valor_dias

    elif quarto == 3:
        quantidade_quartos = int(input('Qual a quantidade de quartos luxo você quer: '))
        disp_lu -= quantidade_quartos
        if disp_st < 0:
            print('Não temos essa quantidade de quartos disponíveis para esse quarto')
        else:
            if quantidade_quartos > maior_quant_reserva:
                maior_quant_reserva = quantidade_quartos
                nome_reserva_mais_cara = nome
            valor_dias = Quantida_de_dias * 250
            total_reservas += valor_dias
    else:
        print('Escolha um tipo de quarto possível')
    reservas += 1
if reservas == 0:
    media_reservas = reservas
else:
    media_reservas = total_reservas / reservas

if reservas >= 1:
    print(f'O total de reservas realizadas = {reservas}')
    print(f'Soma total das reservas = {total_reservas}')
    print(f'Média total das reservas = {media_reservas}')
    print(f'Maior valor de reserva foi de {maior_quant_reserva} e o responsavel é {nome_reserva_mais_cara}')
    print(f"A maior quantida de tempo foi de {maior_tempo} dias. E o responsavel foi {nome_maior_tempo}")
