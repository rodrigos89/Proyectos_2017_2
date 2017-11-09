import pygame as pg
import sys

pg.init()
pantalla = pg.display.set_mode((640, 480))

hecho = False
font = pg.font.SysFont("comicsansms", 36)
text = font.render("Bienvenidos al Workshop DJP usando Pygame", True, (0, 128, 0))

pantalla.fill((255, 255, 255))
pantalla.blit(text, (320 - text.get_width() // 2, 240 - text.get_height() // 2))
pg.display.set_caption("Mi titulo")
pg.display.flip()

while True:
    for evento in pg.event.get():
        if evento.type == 12:
            pg.quit()
            print("Ha cerrado la ventana")
            sys.exit()
        if evento.type == pg.KEYDOWN:
            pg.quit()
            print(evento.type)
            print("Ha cerrado la ventana por scape")
            sys.exit()