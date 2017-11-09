import pygame
import time

pygame.init()
screen = pygame.display.set_mode((300, 300))
done = False

emoji = pygame.image.load('guino.png')  # nuestro emoji
checkers = pygame.image.load('fondo_peq.jpg')  # cargando fondo
emoji1 = pygame.image.load('sad.png')
emoji2 = pygame.image.load('laugh.png')
while not done:
    start = time.time()
    # pump those events!
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = True

    # Estableciendo el fondo
    x = 0
    while x < 300:
        y = 0
        while y < 300:
            screen.blit(checkers, (x, y))
            y += 32
        x += 32

    # Aqui se empieza a graficar
    lista = [emoji, emoji1, emoji2]
    screen.blit(lista[0], (100, 100))
    #screen.blit(lista[1], (120,120))
    pygame.display.flip()

    # Temporizador en Pygame
    # Solo se va a colocar un thread
    end = time.time()
    diff = end - start
    framerate = 30
    delay = 1.0 / framerate - diff
    if delay > 0:
        time.sleep(delay)