# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as
# informações possíveis sobre ele.

# O jeito que eu fiz:
# numero = input("Digite algo: ")
# print(numero.isnumeric())
# print(numero.isalnum())
# print(numero.isalpha())
# print(numero.isascii())
# print(numero.isdigit())
# print(numero.isdecimal())
# print(numero.isidentifier())
# print(numero.islower())
# print(numero.isprintable())
# print(numero.isspace())
# print(numero.istitle())
# print(numero.isupper())

# Professor Guanabara fez assim:

a = input("Digite algo: ")
print("O tipo primitivo desse valor é", type(a)) # A função input retorna sempre str.
print("Só tem espaços? ", a.isspace())
print("É um número?", a.isnumeric())
print("É alfabético?", a.isalpha())
print("É alfanumérico?", a.isalnum())
print("Está em maiúsculas?", a.isupper())
print("Está em minúsculas?", a.islower())
print("Está capitalizada?", a.istitle())






