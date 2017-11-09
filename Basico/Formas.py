import pygame

pygame.init()

window=pygame.display.set_mode((500,400))

pygame.display.set_caption("Formas en Pygame")

#establecer los colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#visible image is Surface
windowSurface=pygame.Surface((500,400))

#Blitting surface no window
window.blit(windowSurface,(0,0))

# Dibuja un circulo azul en el surface con pos (300,50) radio de 20
pygame.draw.circle(windowSurface, BLUE, (50, 50), 45, 0)
pygame.draw.circle(windowSurface, BLUE, (250, 50), 45, 45)#ancho es igual a radio

# Dibuja algunas lineas azules en el surface con inicio y punto final
pygame.draw.line(windowSurface, BLUE, (10, 125), (250, 125), 10)
pygame.draw.line(windowSurface, BLUE, (10, 150), (250, 150), 5)
pygame.draw.line(windowSurface, BLUE, (10, 175), (250, 175), 1)

# Dibuja un elipse rojo al surface
pygame.draw.ellipse(windowSurface, RED, (10, 200, 240, 40), 1)
pygame.draw.ellipse(windowSurface, RED, (10, 250, 240, 40), 0)

# Dibuja el texto background rectangulo en surface
pygame.draw.rect(windowSurface, RED, (375,15,100,100))
pygame.draw.rect(windowSurface, RED, (375,125,100,100),5)

# Dibuja un poligono verde
# pointlist are define in anti-clockwise direction
pygame.draw.polygon(windowSurface, GREEN, ((150, 350), (450, 380), (450, 350), (350, 250), (300, 350)))

window.blit(windowSurface,(0,0))
#window.blit(windowSurface,(100,100))
#Actualizando display
pygame.display.update()
