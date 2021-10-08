'''
Created on 26 jun 2021

@author: CocO
'''
import pygame as pg
import os
import sys
from PokemonPuzzle import moverAbajo, moverArriba, moverIzquierda, moverDerecha
from random import randint

#screen ratio
alto, ancho = 800, 600
#fotograma por segundo(FPS)
fps = 60
#title of window
titulo = "juego demo"
#ventana
screenGame = pg.display.set_mode((alto, ancho))
#imagen PNG
picture = pg.image.load(os.path.join('resources', '1.jpg'))
#sonido
musica = os.path.join(os.getcwd(),'resources/Piquete.mp3')

pg.display.set_caption(titulo)


#cargar musica
def loadSong(musica):
    pg.mixer.init()
    pg.mixer.music.load(musica)
    pg.mixer.music.play(-1)
#actualizar pantalla
def updScreen():
    screenGame.fill((100,255,0))
    screenGame.blit(picture, (alto/4,ancho/4))
    pg.display.update()
    
def main():
    
    #loadSong(musica)
    run = True
    reloj = pg.time.Clock()
        
    while run:
        reloj.tick(fps)
        #por cada evento ocurrido durante la ejecucion
        for evento in pg.event.get():
            #si se presiona el boton rojo x
            if evento.type == pg.QUIT or(evento.type == pg.KEYDOWN and evento.key == pg.K_ESCAPE):
                #cerrar todo
                pg.quit()
                sys.exit()
            pruebamouseClic(evento)
                
        updScreen()

def pruebaTrueWhile():
    while True:
        a, b = 1, 6
        if not a == 6:
            break 
    c= a
        
    print(c)

def armarTableroI(columnas,filas):
    elTablero = []
    casillas = filas*columnas
    
    for i in range(casillas):
        elTablero.append(i)
        
    blanca_index = casillas-1
    elTablero[blanca_index] = -1 
    
    print(elTablero, blanca_index)
    
    for i in range(100):
        print("vuelta ->", i)
        j = randint(0, 3)
        
        if j == 0: blanca_index = moverDerecha(blanca_index, columnas, elTablero)
        elif j == 1: blanca_index = moverArriba(blanca_index, columnas, elTablero)
        elif j == 2: blanca_index = moverAbajo(blanca_index, columnas, elTablero)
        elif j == 3: blanca_index = moverIzquierda(blanca_index, columnas, elTablero)
            
    return elTablero, blanca_index
    
def pruebamouseClic(evento):
    #for evento in pg.event.get():
        if evento.type == pg.MOUSEBUTTONDOWN and evento.button ==1:
            x, y = pg.mouse.get_pos()
            print("x --> ",x)
            print("y --> ",y)
        
def f1(tamanio):
    casillas = tamanio*tamanio
    for i in range(casillas):
        print(i," mod ", tamanio, " = ", i//tamanio) 
class linea:
    #CONSTRUCTOR
    def __init__(self, lenght,origenX, origenY, coordenadas):
        self.lenght = lenght
        self.origenX = origenX
        self.origenY = origenY
        self.coordenadas = coordenadas
if __name__ == '__main__':    
    #main()
    #print(armarTableroI(4, 4))
    #pruebaTrueWhile()
    f1(3)