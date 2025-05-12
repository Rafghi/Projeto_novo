import sys

nome = input("Digite o seu nome:")

if nome == "":
    print("Nome inválido! Nome vazio!")
    sys.exit()

dia_in = int(input("Digite o dia do seu check_in: "))

if dia_in > 31:
    print("Dia inválido! Esse dia não existe!")
    sys.exit()

mes_in = int(input("Digite o mês do seu check_in: "))

if mes_in > 12:
    print("Mês inválido! Esse mês não existe")
    sys.exit()

ano_in = int(input("Digite o ano do seu check_in: "))

dia_out = int(input("Digite o dia do seu check_out: "))

if dia_out > 31:
    print("Dia inválido! Esse dia não existe!")
    sys.exit()

mes_out = int(input("Digite o mês do seu check_out: "))

if mes_out > 12:
    print("Mês inválido! Esse mês não existe")
    sys.exit()
ano_out = int(input("Digite o ano do seu check_out: ")) 

quarto = input("Digite o tipo de quarto (Stardad, Premium, Luxo):")
