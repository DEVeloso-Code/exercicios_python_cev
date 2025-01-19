# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
from tkinter.font import names

nome = input("Escreva seu nome completo: ")
if "Silva" in nome:
    print("Seu nome contém Silva.")
else:
    print("Seu nome não contém Silva.")