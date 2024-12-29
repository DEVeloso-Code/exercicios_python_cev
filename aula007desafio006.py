# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

# Jeito que eu fiz.
n =  int(input("Insira um número: "))
d = n * 2
t = n * 3
p = n ** 2
print("O dobro de {} é {}, o triplo de {} é {} e a raiz quadrada de {} é {}".format(n, d, n, t,
                                                                                    n, p))
# Jeito que o Prof Guanabara fez.
n =  int(input("Insira um número: "))
d = n * 2
t = n * 3
r = n ** (1/2)
print("O dobro de {} vale {}.".format(n, d))
print("O triplo de {} vale {}. \n A raiz quadrada de {} é igual a {:.2f}.".format(n, t, n, r))

# Outra forma do Prof Guanabara.
n =  int(input("Insira um número: "))
print("O dobro de {} vale {}.".format(n, (n*2)))
print("O triplo de {} vale {}. \n A raiz quadrada de {} é igual a {:.2f}.".format(n, (n*3), n,
                                                                                  pow(n, (1/2))))