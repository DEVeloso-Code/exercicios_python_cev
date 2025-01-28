# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma
# mensagem dizendo que ele foi multado.
# A multa vai custar R$7.00 por cada km acima do limite.

# Coleta a velocidade do veículo
velocidade = int(input("Qual a velocidade do carro: "))
# Expressa se a velocidade do veículo for maior que 80 deverá ser aplicado multa * 7
if velocidade > 80:
    multa = velocidade * 7
    print(f"Seu carro estava a {velocidade}Km/h e por isso será multado em R${multa:.2f}.")
else:
    print(f"Seu carro estava a {velocidade}Km/h e por isso não será multado.")





