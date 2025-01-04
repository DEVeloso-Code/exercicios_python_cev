# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de
# aumento.

salario_antigo = float(input("Insira seu salário: R$"))
percentual_aumento = 15 # 15% de aumento salarial.
novo_salario = salario_antigo * percentual_aumento / 100
print(f"O seu salário anterior de R${salario_antigo:.2f} passa ser de R${novo_salario} após o "
      f"reajuste de 15%")