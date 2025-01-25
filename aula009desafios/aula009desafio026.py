# Faça um programa que leia uma frase pelo teclado e mostre.
# 1) Quantas vezes aparece a letra "A".
# 2) Em que posição ela aparece a primeira vez.
# 3) Em que posição ela aparece a última vez.

nome = input("Insira seu nome completo: ")

#1)
if "a" or "A" in nome:
    print("Seu nome contém a vogal 'A'!")
else:
    print("Seu nome não contém a vogal 'A'!")

#2)
quantidade = nome.count("a") + nome.count("A")
print(f"Seu nome possui {quantidade}x a letra 'A'!")

localizacao_ultima_a = nome.rfind("a")
localizacao_ultima_A = nome.rfind("A")

#3)
if localizacao_ultima_a != -1:
    print(f"A letra 'a' aparece pela última vez na localização: {localizacao_ultima_a}")
if localizacao_ultima_A != -1:
    print(f"A letra 'A' aparece pela última vez na localização: {localizacao_ultima_A}")
if quantidade == 0:
    print("Seu nome não possui letra 'A'!")


# Jeito que o prof Guanabara fez

#1)
frase = str(input("Digite uma frase: ")).upper().strip() #Joga todas as letras para maiúsculo +
# Tira espaços indesejados.
print("A letra A aparecer {} vezes na frase".format(frase.count("A")))
print("A primeira letra A apareceu na posição {}".format(frase.find("A")+1))
print("A última letra A apareceu na posição {}".format(frase.rfind("A")+1))

