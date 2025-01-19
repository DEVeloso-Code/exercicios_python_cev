# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# Ex: Digite um número: 1834
# Unidade 4.
# Dezena 3.
# Centena 8.
# Milhar 1.

numero = int(input("Insira um número (de 0 a 9999): "))
numero_str = str(numero).zfill(4)

milhar = numero_str[0]
centena = numero_str[1]
dezena = numero_str[2]
unidade = numero_str[3]

print(f"Milhar: {milhar} \nCentena: {centena} \nDezena: {dezena} \nUnidade: {unidade}")