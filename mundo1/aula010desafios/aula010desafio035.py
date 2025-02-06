# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou
# não formar um triângulo. R1, R2, R3

# Entrada dos comprimentos das retas
r1 = float(input("Digite o comprimento da primeira reta: "))
r2 = float(input("Digite o comprimento da segunda reta: "))
r3 = float(input("Digite o comprimento da terceira reta: "))

# Verificação da condição de existência de um triângulo
if (r1 + r2 > r3) and (r1 + r3 > r2) and (r2 + r3 > r1):
    print("As retas podem formar um triângulo.")
else:
    print("As retas NÃO podem formar um triângulo.")


