import pygame

run = 1
screen = pygame.display.set_mode((250,250))
pygame.display.set_caption("Escuchando los movimientos del Raton")

while run:
    event = pygame.event.poll()
    pos = pygame.mouse.get_pos()
    if event.type == pygame.QUIT:
        run = 0
    elif event.type == pygame.MOUSEMOTION:
        print "Raton en (%d, %d)" % event.pos
    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        print "Clic izquierdo en pos=(%d, %d)" %pos
    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
       print "Clic derecho en pos=(%d, %d)" %pos
    if event.type == pygame.MOUSEBUTTONDOWN:
         print "Boton subir Raton"
    if event.type == pygame.MOUSEBUTTONUP:
         print "Boton bajar Raton"