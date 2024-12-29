# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
from email.quoprimime import header_check
from encodings.cp862 import decoding_map

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
# Feito por mim.
m = float(input("Insira uma distância em metros: "))
km =  m * 0.001
m = m * 1
dm = m * 10
cm = m * 100
mm = m * 1000
print("A medida de {} corresponde a: \n {}km \n {}m \n {}dm \n {}cm \n {}mm".format(m, km, m, dm,
                                                                                    cm, mm))

# Feito por IA
# Entrada do usuário
distancia_metros = float(input("Insira uma distância em metros: "))

# Cálculo das conversões
distancia_km = distancia_metros * 0.001
distancia_dm = distancia_metros * 10
distancia_cm = distancia_metros * 100
distancia_mm = distancia_metros * 1000

# Saída formatada. Utilizando f-strings para formatar mais rápido.
print(f"A medida de {distancia_metros} metros corresponde a: \n" 
      f"{distancia_km} km \n"
      f"{distancia_metros} m \n"
      f"{distancia_dm} dm \n"
      f"{distancia_cm} cm \n"
      f"{distancia_mm} mm")





