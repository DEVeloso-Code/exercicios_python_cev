# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

valor = float(input("Insira o valor o valor do produto: R$"))
desconto = valor - (valor * 0.5)
print(f"O valor do produto desejado é de R${valor}, com o desconto de 5% o novo valor do produto "
      f"é de R${desconto}")
