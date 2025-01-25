# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o
# último nome de separadamente.
# Ex.: Ana Maria de Souza.
# Primeiro = Ana.
# Último = Souza.

nome = input("Insira seu nome: ")
print(nome.split())

# Segundo jeito

name = input("Insira seu nome: ")
names = name.split()
for i, n in enumerate(names):
    print(f"{i + 1}° nome: {n}")

# Jeito que o prof Guanabara fez

# Solicitar ao usuário que digite seu nome completo
no = str(input("Digite seu nome completo: ")).strip()

# Dividir o nome em uma lista
noome = no.split()

# Exibir mensagens
print("Muito prazer em te conhecer!")
print("Seu primeiro nome é {}".format(noome[0]))

# Acessar o último nome corretamente
print("Seu último nome é {}".format(noome[-1]))

