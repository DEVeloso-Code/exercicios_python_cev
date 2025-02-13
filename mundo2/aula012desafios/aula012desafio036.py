# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa
# vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule
# o valor da prestação sabendo que ela não pode exceder 30% do salário ou então o empréstimo será
# negado.

# Entrada de dados
valor_casa = float(input("Qual o valor da casa? R$ "))
salario = float(input("Qual o seu salário? R$ "))
prazo = int(input("Em quantos anos você pretende pagar? "))

# Cálculos
porcentagem_maxima = 30  # 30% do salário
prazo_meses = prazo * 12  # Convertendo anos para meses
valor_parcela = valor_casa / prazo_meses  # Valor da parcela sem considerar o salário
limite_parcela = salario * (porcentagem_maxima / 100)  # 30% do salário

# Verificação
if valor_parcela <= limite_parcela:
    print(f"Empréstimo aprovado! O valor da parcela será de R$ {valor_parcela:.2f} por mês.")
else:
    print(f"Empréstimo negado. O valor da parcela de R$ {valor_parcela:.2f} excede 30% do seu salário.")