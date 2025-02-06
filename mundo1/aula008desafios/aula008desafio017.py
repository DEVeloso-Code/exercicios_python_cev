# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo,
# calcule e mostre o comprimento da hipotenusa.

# Primeira solução:
co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
hi = (co ** 2 + ca ** 2) ** (1/2)
print(f"A hipotenusa vai medir {hi:.2f}")

# Segunda solução - Importando a biblioteca MATH.
import math
cop = float(input("Comprimento do cateto oposto: "))
cad = float(input("Comprimento do cateto adjacente: "))
hi = math.hypot(cop, cad)
print(f"A hipotenusa vai medir {hi:.2f}")
