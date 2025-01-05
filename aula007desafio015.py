# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
# quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro
# custa R$60 por dia e R$0.15 por Km rodado.

# Começo pedindo o total de dias de locação do veículo + total de Km rodados.
dias = int(input("Insira o n° de dias em que o carro esteve alugado: "))
km = float(input("Insira o n° de Km rodados pelo carro alugado: "))
vd = dias * 60 # vd = Valor Dias
vkm = km * 0.15 # vkm = Valor Km
vt = vd + vkm
# print(vt) Inseri um print para testar o valor
print(f"O valor total a ser pago é de R${vt:.2f}, já que foram {dias} dias de locação por R$60.00 a "
      f"diária e {km:.0f}Km por R$0.15 o Km rodado.")

