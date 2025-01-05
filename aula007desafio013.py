# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de
# aumento.

s = float(input("Insira o seu salário base: R$")) # s = Salário.
a = 15 # a = aumento / 15 = 15%.

# Decidi montar uma variável que já faça o cálculo de quanto seriam os 15% + o salário, primeiro
# realizo a operação para descobrir o valor do reajuste, de acordo com o salário, e depois somo
# esse valor a ele.

ns = s + (s * a / 100) # ns = Novo Salário.
# print(ns) = testei o resultado de ns para saber se estava gerando o aumento de 15% direto no
# salário.

# Faço um print mostrando para a pessoa o salário que ela digitou + o novo salário com o reajuste.
print(f"O seu salário atual de R${s:.2f} com o reajuste de 15% passa a ser: R${ns:.2f}. Faça bom "
      f"proveito do seu aumento!")
