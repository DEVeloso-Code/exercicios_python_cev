# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

# Jeito que eu fiz.

valor = float(input("Insira o valor o valor do produto: R$")) # Solicito o valor do produto.
percentual_desconto = 5 # 5% é o valor da percentual
desconto = valor - (valor * percentual_desconto / 100) # Operação per centual
print(f"O valor do produto desejado é de R${valor:.2f}, com o desconto de 5% o novo valor do "
      f"produto "
      f"é de R${desconto:.2f}")

# Jeito que o prof Guanabra fez

preco = float(input("Qual é o preço do seu produto? R$"))
novo = preco - (preco * 5 / 100)
print("O produto que custava R${}, na promoção com desconto de 5% vai custar R${}".format(preco,
                                                                                          novo))