# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.500.00 calcule um aumento de 10%
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input("Insira seu salário: "))
if salario >= 1500:
    aumento = salario * 1.10
    print(f"Seu novo salário será de R${aumento:.2f}")
else:
    aumento2 = salario * 1.15
    print(f"Seu novo salário será de R${aumento2:.2f}")
