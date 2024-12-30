# Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada.
from dataclasses import replace

n = int(input("Digite um número para ver sua tabuada: "))
print(f"Os resultados são: \n {n} x 1 = {n*1} \n {n} x 2 = {n*2} \n {n} x 3 = {n*3} "
      f"\n {n} x 4 = {n*4} \n {n} x 5 = {n*5} \n {n} x 6 = {n*6} \n {n} x 7 = {n*7} \n"
      f" {n} x 8 = {n*8} \n {n} x 9 = {n*9} \n {n} x 10 = {n*10}")

# Jeito que o prof Guanabara fez.

num =  int(input("Digite um número para ver sua tabuada: "))
print("{} x {} = {}".format(num, 1, num*1))
print("{} x {} = {}".format(num, 2, num*2))
print("{} x {} = {}".format(num, 3, num*2))
print("{} x {} = {}".format(num, 4, num*4))
print("{} x {} = {}".format(num, 5, num*5))
print("{} x {} = {}".format(num, 6, num*6))
print("{} x {} = {}".format(num, 7, num*7))
print("{} x {} = {}".format(num, 8, num*8))
print("{} x {} = {}".format(num, 9, num*9))
print("{} x {} = {}".format(num, 10, num*10))
print('-'*12)