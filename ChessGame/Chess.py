import pygame, sys, re
from Pieces import Piece


pygame.init() #Initialize pygame


window_size = width, height = 512, 512
screen = pygame.display.set_mode(window_size)


class Chessboard():
    def __init__(self) -> None:
        self.chessboard = pygame.image.load("src/Chessboard.png")
        self.chessboard.convert()
        self.chessboardtxt = open("src/chessboard.txt", "r")

    def addPieces(self) -> list:
        self.pieces = []
        self.nestedpieces = []
        for rows in self.chessboardtxt:
            for x in rows:
                if (re.search("[a-zA-Z]", x)):
                    if x == "p":
                        self.nestedpieces.append(Piece.Pawn(1, len(self.nestedpieces), len(self.pieces)))
                    elif x == "P":
                        self.nestedpieces.append(Piece.Pawn(-1, len(self.nestedpieces), len(self.pieces)))
                    elif x == "h":
                        self.nestedpieces.append(Piece.Knight(1, len(self.nestedpieces), len(self.pieces)))
                    elif x == "H":
                        self.nestedpieces.append(Piece.Knight(-1, len(self.nestedpieces), len(self.pieces)))
                    elif x == "b":
                        self.nestedpieces.append(Piece.Bishop(1, len(self.nestedpieces), len(self.pieces)))
                    elif x == "B":
                        self.nestedpieces.append(Piece.Bishop(-1, len(self.nestedpieces), len(self.pieces)))
                    elif x == "r":
                        self.nestedpieces.append(Piece.Rook(1, len(self.nestedpieces), len(self.pieces)))
                    elif x == "R":
                        self.nestedpieces.append(Piece.Rook(-1, len(self.nestedpieces), len(self.pieces)))
                    elif x == "q":
                        self.nestedpieces.append(Piece.Queen(1, len(self.nestedpieces), len(self.pieces)))
                    elif x == "Q":
                        self.nestedpieces.append(Piece.Queen(-1, len(self.nestedpieces), len(self.pieces)))
                    elif x == "k":
                        self.nestedpieces.append(Piece.King(1, len(self.nestedpieces), len(self.pieces)))
                    elif x == "K":
                        self.nestedpieces.append(Piece.King(-1, len(self.nestedpieces), len(self.pieces)))
                elif x == "0":
                    self.nestedpieces.append(Piece.NullPiece(1, len(self.nestedpieces), len(self.pieces)))
                elif x == "\n":
                    self.pieces.append(self.nestedpieces)
                    self.nestedpieces = []
        self.pieces.append(self.nestedpieces)
        return self.pieces
        
    
    def draw(self, screen) -> None:
        screen.blit(self.chessboard, (0,0)) #Blits the chessboard
        for rows in self.pieces:
            for piece in rows:
                piece.draw(screen)    
    

chessboard = Chessboard()
print(chessboard.addPieces())
while True:
    chessboard.draw(screen)

    mousepos = pygame.mouse.get_pos()
    rect = (chessboard.pieces[1][1]).getRect()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                print("Hei")

    pygame.display.update()



