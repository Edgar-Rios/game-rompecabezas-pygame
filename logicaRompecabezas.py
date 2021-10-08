'''
Created on 30 jun 2021



 0  1  2  3  4
 5  6  7  8  9
10 11 12 13 14
15 16 17 18 19 
20. 21 22 23 24  


columnas = 3
blanca   = 5

@author: Lenovo
'''
'''

_l :text label

1-  mpstrar pantalla de inicio
1.1 pedir tamsño de puzzle
1.2 crear tablero con dimensiones 
2-  traer imagen aleatoria
2.1 dividirla en proporcion del puzzle
3 movimientos de casillas
4 controlar ganador
5 game over

'''

import os
import sys
import cfg
import pygame as pg
import random

TITULO_VENTANA = "juego del 15"
TITULO_JUEGO   = "Rompecabezas o algo asi"

def juegoTerminado(elTablero, nro_columnas, filas):
    assert isinstance(nro_columnas, int) and isinstance(filas, int) 
    num_cells = nro_columnas*filas
    for i in range(num_cells-1):
        if elTablero[i] != i: return False
    return True
    
#3 movimientos
def moverDerecha(blanca_index, nro_columnas, elTablero):
    if blanca_index % nro_columnas == 0: return blanca_index
    elTablero[blanca_index-1], elTablero[blanca_index] = elTablero[blanca_index] ,elTablero[blanca_index-1]
    return blanca_index-1

def moverIzquierda(blanca_index, nro_columnas,elTablero):
    if (blanca_index+1) % nro_columnas == 0: return blanca_index 
    elTablero[blanca_index+1], elTablero[blanca_index] = elTablero[blanca_index] ,elTablero[blanca_index+1] 
    return blanca_index+1

def moverAbajo(blanca_index, nro_columnas, elTablero):
    if blanca_index-nro_columnas < 0: return blanca_index
    elTablero[blanca_index-nro_columnas], elTablero[blanca_index] = elTablero[blanca_index], elTablero[blanca_index-nro_columnas]
    return blanca_index-nro_columnas
'''
0  | 1  | 2.  
3  | 4  | 5  
6  | 7  | 8.  
'''
def moverArriba(blanca_index, nro_columnas, elTablero):
    #if blanca_index >= (nro_columnas-1)*nro_columnas: return blanca_index
    if blanca_index + nro_columnas >= len(elTablero): return blanca_index
    elTablero[blanca_index + nro_columnas], elTablero[blanca_index] = elTablero[blanca_index], elTablero[blanca_index+nro_columnas]
    return blanca_index + nro_columnas

##

def armarTablero(nro_columnas, nro_filas):
    tablero = []
    casillas = nro_filas*nro_columnas
    for i in range(casillas):tablero.append(i)
    
    blanca_index = casillas-1
    tablero[blanca_index] = -1
    
    #mezclar piezas
    for i in range(1000):
        
        direccion = random.randint(0, 3)
        
        if direccion == 0: blanca_index = moverIzquierda(blanca_index, nro_columnas, tablero)
        elif direccion == 1: blanca_index = moverDerecha(blanca_index, nro_columnas, tablero)
        elif direccion == 2: blanca_index = moverArriba(blanca_index, nro_columnas, tablero)
        elif direccion == 3: blanca_index = moverAbajo(blanca_index, nro_columnas, tablero)           
        
    return tablero, blanca_index

def rutaImagenAleatoria(directorio):
    lista_nombres = os.listdir(directorio)
    assert len(lista_nombres) > 0
    return os.path.join(directorio, random.choice(lista_nombres))

def gameOverInterface(screen, ancho, alto):
    screen.fill(cfg.COLOR_DE_FONDO)
    fuente = pg.font.Font(cfg.PATH_DE_FUENTE, ancho//15)
    game_over_l = fuente.render("Enhorabuena! Ganaste!", True, cfg.ROJO)
    rect_go = game_over_l.get_rect()
    rect_go.midtop = (ancho/2, alto/2.5)
    
    info_l = fuente.render("Volver a empezar? s/n", True, cfg.VERDE)
    rect_i = info_l.get_rect()
    rect_i.midtop = (ancho/2, (alto/2.5)-100)
    
    screen.blit(info_l, rect_i)
    screen.blit(game_over_l, rect_go)
    
    while True:
        for evento in pg.event.get():    
            if evento.type == pg.QUIT or (evento.type == pg.QUIT and evento.type == pg.KEYDOWN) or ((evento.key == ord('n') or evento.key == ord('N')) and evento.type == pg.KEYDOWN):
                pg.quit()
                sys.exit()
            elif evento.type == pg.KEYDOWN:
                if (evento.key == ord('s') or evento.key == ord('S')) and evento.type == pg.KEYDOWN:
                    main()
                    
    pg.display.update()
    ###

def MenuPrincipal(screen, ancho, alto) -> int: 
    screen.fill(cfg.COLOR_DE_FONDO)
    fuente_G = pg.font.Font(cfg.PATH_DE_FUENTE, ancho//10)
    fuente_M = pg.font.Font(cfg.PATH_DE_FUENTE, ancho//30)
    
    welcome_l = fuente_G.render(TITULO_JUEGO, True, cfg.AZUL)
    rect_w = welcome_l.get_rect()
    rect_w.midtop = (ancho/2, alto/10)
    
    info_l = fuente_M.render("presione 'P' --> pequeño, 'M' --> mediano, 'G'-> grande>", True, cfg.VERDE)
    rect_i = info_l.get_rect()
    rect_i.midtop = (ancho/2, alto/2)
    
    screen.blit(welcome_l, rect_w)
    screen.blit(info_l, rect_i)
    while True:
        for evento in pg.event.get():
            print(evento)
            if evento.type == pg.QUIT or (evento.type == pg.KEYDOWN and evento.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif evento.type == pg.KEYDOWN:
                if evento.key == ord('p'): return 3
                elif evento.key == ord('m'): return  4
                elif evento.key == ord('g'): return 5
        
        pg.display.update()
        ###      

def main():
    pg.init()
    reloj = pg.time.Clock()
    imagenAleatoria = pg.image.load(rutaImagenAleatoria(cfg.DIRECTORIO_DE_IMAGENES))
    imagenAleatoria = pg.transform.scale(imagenAleatoria, cfg.RESOLUCION_DE_PANTALLA)
    rect_ia = imagenAleatoria.get_rect()
    #rect_ia.center
     
    screen = pg.display.set_mode(cfg.RESOLUCION_DE_PANTALLA)
    pg.display.set_caption(TITULO_VENTANA)
    
    tamaño = MenuPrincipal(screen, 800, 600)#)
    print("el tamaño es ",tamaño)
    columnas, filas = tamaño, tamaño
    print("numero de columnas y filas: ",columnas, filas)
    assert isinstance(columnas, int) and isinstance(filas, int) 
    num_cells = columnas*filas
    print("cantidad total de celdas",num_cells)
    ancho_cell = rect_ia.width//columnas
    alto_cell = rect_ia.height//filas
    '''
    x -->  422 -> x_p = 1.5=1
    y -->  319 -> y_p = 1.5=1
    x + y*size = _4_
    
    x -->  439 -> x_p = 1.6=1
    y -->  514 -> y_p = 2.5=2
    x + y*size = _7_   
    
    '''
    
    while True:
        tablero, blanca_index = armarTablero(columnas, filas)
        if not juegoTerminado(tablero, columnas, filas):
            break    

    run = True

    while run:
        
        for evento in pg.event.get():
            if evento.type == pg.QUIT or (evento.type == pg.KEYDOWN and evento.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            #if evento.type == pg.KEYDOWN
            elif evento.type == pg.KEYDOWN:
                if evento.key == ord('s') or evento.key == pg.K_DOWN:
                    blanca_index = moverAbajo(blanca_index, tamaño, tablero)
                elif evento.key == ord('w') or evento.key == pg.K_UP:
                    blanca_index = moverArriba(blanca_index, tamaño, tablero)
                elif evento.key == ord('a') or evento.key == pg.K_LEFT:
                    blanca_index = moverIzquierda(blanca_index, tamaño, tablero) 
                elif evento.key == ord('d') or evento.key == pg.K_RIGHT:
                    blanca_index = moverDerecha(blanca_index, tamaño, tablero)  
            elif evento.type == pg.MOUSEBUTTONDOWN and evento.button == 1:
                x, y = pg.mouse.get_pos()
                x_columna = x//ancho_cell
                y_fila = y//alto_cell
                cell_index = x_columna + y_fila*tamaño
                if cell_index == blanca_index - 1: 
                    blanca_index = moverDerecha(blanca_index, tamaño, tablero)
                if cell_index == blanca_index + 1: 
                    blanca_index = moverIzquierda(blanca_index, tamaño, tablero)
                if cell_index == blanca_index - tamaño: 
                    blanca_index = moverAbajo(blanca_index, tamaño, tablero)
                if cell_index == blanca_index + tamaño: 
                    blanca_index = moverArriba(blanca_index, tamaño, tablero)
                        
        if juegoTerminado(tablero, columnas, filas):
            tablero[blanca_index] = -1
            run = False
        
        screen.fill(cfg.COLOR_DE_FONDO)
        for i in range(num_cells):
            if tablero[i] == -1:
                continue
            x_columna = i//tamaño
            y_fila = i%tamaño
            
            #linea divisoria de los cuadros
            rect = pg.Rect(y_fila*ancho_cell, x_columna*alto_cell, ancho_cell, alto_cell)
            area_imagen_casilla = pg.Rect((tablero[i]%tamaño)*ancho_cell, (tablero[i]//tamaño)*alto_cell, ancho_cell, alto_cell)
            
            screen.blit(imagenAleatoria, rect, area_imagen_casilla)
            
        for i in range(tamaño+1):
            pg.draw.line(screen, cfg.COLOR_DE_FONDO, (i*ancho_cell, 0), (i*ancho_cell, rect_ia.height))
        for i in range(tamaño+1):
            pg.draw.line(screen, cfg.COLOR_DE_FONDO, (0, i*alto_cell), (rect_ia.width, i*alto_cell))
        
        pg.display.update()
        reloj.tick(cfg.FPS)
        
    gameOverInterface(screen, rect_ia.width, rect_ia.height)
                
