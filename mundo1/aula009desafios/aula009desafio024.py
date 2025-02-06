# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = input("Insira o nome da cidade: ")
if "Santo" in cidade:
    print("A cidade contém 'Santo'")
else:
    print("A cidade não contém 'Santo'")

# Jeito que o prof Guanabra fez.

cid = str(input("Em que cidade você nasceu: ")).strip() # Strip elimina os espaços.
print(cid[:5] == "Santo")