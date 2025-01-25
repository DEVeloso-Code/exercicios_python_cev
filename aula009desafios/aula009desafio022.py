# Crie um programa que leia o nome completo de uma pessoa e mostre:
# 1) O nome com todas as letras maiúsculas.
# 2) O nome com todas as letras minúsculas.
# 3) Quantas letras possui (sem considerar espaços).
# 4) Quantas letras A tem o primeiro nome.

nome = input("Insira o seu nome: ")
print(nome.upper()) # Letras Maiúsculas
print(nome.lower()) # Letras Minúsculas

quantidade_letras = len(nome) # Faz a contagem das letras (incluindo o espaço entre nome e
# sobrenome).
print(quantidade_letras)

quantidade_letras_sem_espaco = len(nome.replace(" ", "")) # Faz a contagem das letras sem contar
# o espaço, isso porque foi substituído" "(com espaço) por "" (sem espaço) utilizado o replace.
print(quantidade_letras_sem_espaco)

quantidade_letras_a = nome.count("a") # Conta a quantidade de letras específicas de um nome.

# Jeito que o prof° Guanabara fez.
n = str(input("Digite seu nome completo: ")).strip() #Elimina os espaços na contagem.
print("Analisando seu nome...")
print("Seu nome em maiúsculas é {}".format(n.upper()))
print("Seu nome em minúsculas é {}".format(n.lower()))
print("Seu nome ao todo tem {} letras".format(len(n) - n.count(" ")))
# print("Seu primeiro nome tem {} letras".format(n.find(" ")))
separa = n.split()
print("Seu primeiro nome é {} e ele tem {} letras.".format(separa[0], len(separa[0])))


