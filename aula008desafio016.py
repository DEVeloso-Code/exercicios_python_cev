# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção
# inteira. Ex: Digite um número: 6.127. O n° 6.127 tem a parte inteira 6. Olhar funções da
# biblioteca MATH.

import math
n = float(input("Insira um número com diversos dígitos: "))
n_inteiro = math.floor(n)
print(f"O seu número arredondado é: {n_inteiro}")

# Esse exercício poderia ser feito com a função int, mas o professor pediu que fosse feito com a
# biblioteca.
