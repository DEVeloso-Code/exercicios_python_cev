#  Escreva um programa que faça o computador "pensar" em um número de 0 a 5 e peça para o usuário
#  tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na
#  tela se o usuário venceu ou perdeu.

# Importa a biblioteca random
import random

# Determina um intervalo de 1 a 5 onde o computador escolhe um número.
numero_secreto = random.randint(1, 5)

numero = int(input("Escolha um número de 1 a 5: "))

if numero == numero_secreto:
    print("Parabéns, você acertou!")
else:
    print(f"Você errou! O número secreto era {numero_secreto}")