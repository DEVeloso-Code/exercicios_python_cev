# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e o seu antecessor.

# Jeito que eu fiz.
n = int(input("Insira um número: "))
a = n - 1
s = n + 1
print("O antecessor do valor {} é {}, o sucessor é {}".format(n, a, s))

# Jeito Prof Guanabara.
n = int(input("Insira um número: "))
print("O antecessor do valor {} é {}, o sucessor é {}".format(n, (n-1), (n+1)))