# Desenvolva um programa que pergunte a distância de uma viagem em KM. Calcule o preço da
# passagem, cobrando R$0.50 por KM para viagens de até 200Km e R$0.45 para viagens mais longas.

# Coleta a distância percorrida de uma viagem
distancia = int(input("Qual será a distância em Km percorrida por você nesta viagem? "))
if distancia <= 200:
    passagem = distancia * 0.50
    print(f"Sua passagem custará R${passagem:.2f}.")
else:
    passagem2 = distancia * 0.45
    print(f"Sua passagem custará R${passagem2:.2f}.")


