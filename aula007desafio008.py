# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

# Jeito que eu fiz.
m = int(input("Insira quantos metros: "))
cm = m * 100
mm = m * 1000
print(f"{m} metros tem {cm}cm ou {mm}mm")

# Jeito que o Prof Guanabara fez.
medida = float(input("Uma distância em metros: "))
cm = medida * 100 # centimetros
mm = medida * 1000 # milimetros
print("A medida de {}m corresponde a {:.0f}cm e {:.0f}mm".format(medida, cm, mm)) # {:.0f} para
# não pular nenhum digito após o ponto.

# Novo desafio: Quilômetro, hectômetro, decâmetro, metro, decímetro, centímetro e milímetro.




