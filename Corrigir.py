# entrada de dados
nome = input("Digite seu nome: ")
checkin_dia = int(input("Coloque o dia: "))
checkin_mês = int(input("Coloque o mês: "))
checkin_ano = int(input("Coloque o ano: "))
checkout_dia = int(input("coloque o check out dia: "))
checkout_mês = int(input("coloque o check out mês: "))
checkout_ano = int(input("coloque o check out ano: "))
quarto = input("qual quarto?: ")

checkin_diafinal = checkin_dia
checkin_mêsfinal = checkin_mês
checkin_anofinal = checkin_ano
checkout_diafinal = checkout_dia
checkout_mêsfinal = checkout_mês
checkout_anofinal = checkout_ano

# validação das entradas
if nome == "":
    print("erro, namedigit: nome vazio")
    quit
if nome.isdigit():
    print("erro, namedigit: nome contem numero")
    quit
if checkin_dia == "" and checkin_mês == "" and checkin_ano == "" and checkout_dia == "" and checkout_mês == "" and checkout_ano == "":
    print("erro, check-in and check-out: check in e check out vazio")
    quit
if checkin_dia == "" and checkin_mês == "" and checkin_ano == "":
    print("erro, check-in: check in vazio")
    quit
if checkout_dia == "" and checkout_mês == "" and checkout_ano == "":
    print("erro, check-out: check out vazio")
    quit
if checkin_dia > 31 and checkin_dia < 1:
    print("erro, check-in-day: numero tem que estar em 1 e 31 dias")
    quit
if checkin_mês > 12 and checkin_mês < 1:
    print("erro, check-in-month: numero tem que estar entre 1 a 12 meses")
    quit
if checkout_dia > 31 and checkout_dia < 1:
    print("erro, check-out-day: numero tem que estar em 1 e 31 dias")
    quit
if checkout_mês > 12 and checkout_mês < 1:
    print("erro, check-out-month: numero tem que estar entre 1 a 12 meses")
    quit
if checkout_ano < checkin_ano:
    print("Erro, ano do check-in é maior do que checkout")
if checkout_mês < checkout_mês and checkin_ano == checkout_ano:
    print("Erro, mês do check-in é maior do que checkout")
if checkout_dia < checkout_dia and checkin_mês == checkout_mês and checkin_ano == checkin_ano:
    print("Erro, dia do check-in é maior do que checkout")

# numero de diarias
dias_passados_checkin = (checkin_ano * 365)+((checkin_mês - 1) * 30) + checkin_dia
dias_passados_checkout = (checkout_ano * 365)+((checkout_mês - 1) * 30) + checkout_dia
total_de_dias = (dias_passados_checkout - dias_passados_checkin)
print(total_de_dias)
standard = 100*total_de_dias
premium = 180*total_de_dias
luxo = 250*total_de_dias

if quarto == "standard" or quarto == "premium" or quarto == "luxo":

    if quarto == "standard":
        preço= standard
    elif quarto == "premium":
        preço= premium
    else:
        preço= luxo

    print(f"\n\nnome da reserva: {nome}. \ndata de check in: {checkin_diafinal}/{checkin_mêsfinal}/{checkin_anofinal}. \ndata de checkout: {checkout_diafinal}/{checkout_mêsfinal}/{checkout_anofinal}. \ntotal de dias: {total_de_dias}. \npreço: R${preço}")

elif quarto == "":
    print("erro, nome do quarto vazio")
    quit
else:
    print("quarto não encontrado, tente novamente.")
    quit
