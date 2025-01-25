# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
from tkinter.font import names

# Jeito que eu fiz
nome = input("Escreva seu nome completo: ")
if "Silva" in nome:
    print("Seu nome contém Silva.")
else:
    print("Seu nome não contém Silva.")

# Jeito que o prof Guanabara fez

nome = str(input("Qual é seu nome completo: ").strip())
print("Seu nome tem Silva? {}".format("silva" in nome.lower())) #in é um operador do Python