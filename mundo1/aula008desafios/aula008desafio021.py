# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame

# Inicializar o mixer do pygame
pygame.init()

# Carregar o arquivo MP3
pygame.mixer.music.load("aula008desafio021arquivo.mp3")

# Tocar o arquivo MP3
pygame.mixer.music.play()

# Manter o programa rodando até o fim do áudio
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)


