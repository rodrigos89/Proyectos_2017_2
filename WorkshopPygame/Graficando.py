import pygame

#Inicializando modulo
pygame.init()

#creando el canvas para dibujar una imagen
#visible en un parte de la pantalla
#Esta funcion crea un Surface
window=pygame.display.set_mode((250,250))

pygame.display.set_caption("Graficando en Pygame")

#Imagen visible
one_surface=pygame.Surface((75,75))
two_surface=pygame.Surface((200,200))

#Llenando el surface
one_surface.fill((255,255,255)) #white
two_surface.fill((0,255,0)) #white

#Combinando los surface en la ventana
window.blit(one_surface,(0,0))
window.blit(two_surface,(75,75))

#Actualizando display surface
pygame.display.update()

run=True
while run:
 for event in pygame.event.get():
  if event.type ==pygame.QUIT:
   run=False
