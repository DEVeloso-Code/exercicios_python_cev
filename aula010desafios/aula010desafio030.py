#  Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

# Solicitar um número qualquer.
numero = int(input("Insira aqui seu número: "))

# Definir se o número é par ou ímpar.
if numero % 2 == 0:
    print(f"O número {numero} é PAR!")
else:
    print(f"O número {numero} é ÍMPAR!")
