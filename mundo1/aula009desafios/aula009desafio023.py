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

# Jeito que o prof Guanabara fez.

num = int(input("Informe um número: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print("Analisando o número {}".format(num))
print("Unidade: {}".format(u))
print("Dezena: {}".format(d))
print("Centena: {}".format(c))
print("Milhar: {}".format(m))

# Nesse caso se não houver centena e milhar, o resultado será 0.
