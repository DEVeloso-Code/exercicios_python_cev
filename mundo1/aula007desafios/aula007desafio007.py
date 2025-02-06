# Desenvolva um programa que que leia as duas notas de um aluno, calcule e mostre sua média.

# Jeito que eu fiz.
nota1 = int(input("Insira a primeira nota do aluno: ")) # O int não irá permitir notas flutuantes.
nota2 = int(input("Insira a segunda nota do aluno: ")) # O int não irá permitir notas flutuantes.
soma = nota1 + nota2
media = soma / 2
print("A nota média do aluno é {}".format(media))

# Segundo jeito que eu fiz.
nota1 = float(input("Insira a primeira nota do aluno: ")) # float por ser um n° flutuante.
nota2 = float(input("Insira a segunda nota do aluno: ")) # float por ser um n° flutuante.
media = (nota1 + nota2) / 2
print("A nota média do aluno é {}".format(media))

# Jeito que o Prof Guanabara fez.
n1 = float(input("Insira a primeira nota do aluno: ")) # float por ser um n° flutuante.
n2 = float(input("Insira a segunda nota do aluno: ")) # float por ser um n° flutuante.
m = (n1 + n2) / 2
print("A média entre {:.1f} e {:.1f} é igual a {:.1f}!".format(n1, n2, m)) # {:.1f} = toda conta
# será representa com 1 digito após o ponto.

