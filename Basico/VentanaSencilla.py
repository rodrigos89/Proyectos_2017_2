import pygame as pg
import sys

#1. Creando una ventana y controlando evento salir
pg.init()
ventana = pg.display.set_mode((200,300))
pg.display.set_caption("Bienvenidos a mi Workshop")

while True:
    for evento in pg.event.get():
        if evento.type == 12:
            pg.quit()
            print("Ha cerrado la ventana")
            sys.exit()
    pg.display.update()