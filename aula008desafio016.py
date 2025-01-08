# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção
# inteira. Ex: Digite um número: 6.127. O n° 6.127 tem a parte inteira 6. Olhar funções da
# biblioteca MATH.

import math
n = float(input("Insira um número: "))
n_inteiro = math.floor(n) # Floor sempre arredonda para baixo.
print(f"O seu número inteiro é: {n_inteiro}")

# Esse exercício poderia ser feito com a função int, mas o professor pediu que fosse feito com a
# biblioteca.

# Jeito que o prof Guanabara fez.
import math
num = float(input("Digite um valor: "))
print("O valor digitado foi {} e a sua porção inteira é {}".format(num,math.trunc((num))))

# Jeito que eu fiz para otimizar o código.
from math import trunc # Importo apenas a funcionalidade dentro do Python.
nm = float(input("Digite um valor: "))
print(f"O valor digitado foi {nm} e sua porção inteira é {trunc(nm)}.")

# 2 jeito que o prof Guanabara fez, sem importar nada
numero = float(input("Digite um valor: "))
print("O valor digitado foi {} e a sua porção inteira é {}".format(numero, int(numero))) #
# Formatando o n° inteiro não existe a necessidade de se importar uma biblioteca.


