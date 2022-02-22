import pygame, sys

pygame.init()

window_size = width, height = 512, 512

screen = pygame.display.set_mode(window_size)

chessboard = pygame.image.load("ChessGame/src/Chessboard.png")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    screen.blit(chessboard, (0,0))
    pygame.display.update()



