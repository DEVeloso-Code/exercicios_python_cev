# Escreva um programa que converta uma temperatura digitada de °C para °F.

c = float(input("Insira a temperatura em °C:")) # c = Celsius.
f = float(input("Insira a tempora em °F:")) # f = Fahrenheit.

# Abaixo irei realizar as fórmulas para converter ambas as temperaturas.
c2f = c * (9/5) + 32 # (9/5) + 32 é a fórmula utilizada na conta de conversão de °C para °F.
f2c = (f - 32) * 5 / 9 # Nesse caso a conversão se inverte.
# print(conversao) = Fiz um teste para saber se o resultado está correto. Resultado positivo.

# Abaixo faço um print individual para cada conversão. No °F adicionei :.1f por ser uma operação
# que necessita de mais um digito, já que a temperatura contém essa fórmula.
print(f"Sua temperatura atual em °C é {c:.0f}°C, que convertida para Fahrenheit é {c2f:.1f}°F")
print(f"Sua temperatura atual em °F é {f:.1f}°F, que convertida para Celsius é {f2c:.0f}°C")

# Jeito que o prof Guanabara fez.

cels = float(input("Informe a temperatura em °C: "))
fahr = 9 * cels / 5 + 32 # Ordem de precedência funcionando.
print("A temperatura de {}°C corresponde a {}°F!".format(cels, fahr))
