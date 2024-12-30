# Crie um programa que leia quanto dinheiro a pessoa tem na carteira e mostre quantos dólares ela
# pode comprar - considerar US$1.00 = R$5.00.

# Jeito que eu fiz.
real = float(input("Insira quantos reais você possui na carteira: R$"))
dolar = 6.00
print(f"O valor atual do dólar é de US${dolar:.2f} por dólar, sua carteira possui R${real:.2f} é "
      f"possível comprar US${real/dolar:.3}")

# Jeito que o prof Guanabara fez.
real = float(input("Quanto dinheiro você tem na carteira? R$"))
dolar = real / 6.00
print("Com R${:.2f} você pode comprar US${:.2f}".format(real, dolar))


