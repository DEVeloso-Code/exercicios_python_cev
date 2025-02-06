# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e
# tangente desse ângulo.

import math
angulo = float(input("Digite o ângulo que você deseja: "))
seno = math.sin(math.radians(angulo)) # Pega o ângulo digitado e converte para radianos.
print(f"O ângulo de {angulo} tem o SENO de {seno:2.f}")
cosseno = math.cos(math.radians(angulo)) # Pega o cosseno e converte para radians.
print(f"O ângulo de {angulo} tem o COSSENO de {cosseno:.2f}")
tangente = math.tan(math.radians(angulo)) # Pega a tangente e converte para radians.
print(f"O ângulo de {angulo} tem a TANGENTE de {tangente:.2f}")

# Poderia ser importado apenas as funcionalidades dentro da biblioteca.
# from math import radians, sin, cos, tang