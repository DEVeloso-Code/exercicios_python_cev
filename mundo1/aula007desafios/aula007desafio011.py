# Faça um programa que leia a altura e a largura de uma parede em metros, calcule a sua área e a
# quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de
# 2m².

# Cálculo: Medir a altura pela largura para obter a área total

lar = float(input("Insira a altura da parede: "))
alt = float(input("Insira a largura da parede: "))
area = lar * alt
print(f"Sua parede tem a dimensão de {lar:.2f} x {alt:.2f} e sua área é de {area:.2f}m²")
tinta = area / 2
print(f"Para pintar essa parede você precisará de {tinta}l de tinta.")

