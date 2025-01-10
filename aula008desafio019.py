# Um professor quer sortear um dos seus 4 alunos para apagar o quadro. Faça um programa que ajude
# ele, lendo o nome deles e escrevendo o nome do escolhido. Biblioteca RANDOM.

import random # Importa o randomizador de elementos.
# from random import choice - Faz a importação apenas da funcionalidade choice.
n1 = str(input("Primeiro aluno: "))
n2 = str(input("Segundo aluno: "))
n3 = str(input("Terceiro aluno: "))
n4 = str(input("Quarto aluno: "))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista) # Faz uma escolha no item escolhido, nesse caso a lista.
print(f"O aluno escolhido foi {escolhido}")
