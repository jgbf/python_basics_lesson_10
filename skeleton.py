# hasznaljuk a pygame libraryt
import pygame
# hasznaljuk az osszes erteket a locals filebol pl.: gombok kezelese
from pygame.locals import *

# Kotelezo lepes a pygame lib hasznalatanal ez allitja ossze az alapokat
pygame.init()

# Beallitjuk az abalak mereteit es feliratait
WIDTH, HEIGHT = 900, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Labda')

ball = pygame.image.load('ball.png')
ball_h = 100
ball_w = 100
ball = pygame.transform.scale(ball, (ball_h, ball_w))

# Itt definialjuk a konstansokat
WHITE = (255, 255, 255)
VEL = 1
FPS = 60

# Segitseg az iranyitashoz 
pygame.key.set_repeat(1)

def main():
    # Beallitjuk a kepkocka sebesseget, mert kulonbozo CPU-kon kolonbozo 
    # sebesseggel futhat a jatek
    clock = pygame.time.Clock()

    ball_rect = pygame.Rect(300, 400, ball_w, ball_w)

    # Vegtelen ciklus, ami eletben tarja az ablakot, egyebkent rogton bezarodna 
    # az ablaak, amit fent letrehoztunk, mert veget erna a program
    run = True
    while run:
        # Itt tartjuk kordaban az FPS-t
        clock.tick()
        # Itt ellenorizzuk hogy tortent-e valamilyen esemeny ez az esemeny lehet 
        # gombnyomas, eger mozgatas, kattintas, ablak mozgatas
        for event in pygame.event.get():
            # Ez az if ellenorzi, h rakattintottunk-e az x gombra az ablakon
            if event.type == pygame.QUIT:
                # Ha rakattintunk az x-re, akkor vege a vegtelen ciklusnak
                run = False


        # Beallitjuk a hatterer szinet
        WIN.fill(WHITE)

        WIN.blit(ball, (ball_rect.x, ball_rect.y))

        # Frissitjuk a teljes kepernyot, hogy ha valtozna valami akkor az megjelenjen
        pygame.display.update()

    # Lezarjuk az inicializalt funkciokat ,amit a pygame.init() letrehozott
    pygame.quit()

# Futtatjuk a fenti main fugvenyt, ha ezt a fajlt futtatjuk
if __name__ == '__main__':
    main()

