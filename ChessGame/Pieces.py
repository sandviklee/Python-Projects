import pygame    

class Piece:
    class BasePiece:
        def __init__(self, _color: int, x: int, y: int) -> None:
            self._moved = False
            
            if not _color in [-1, 1]:
                raise ValueError('invalid _color attribute value')
            
            self._color = _color

            if x not in range(8) or y not in range(8):
                print(x, y)
                raise ValueError('x and y must be integers')
            
            self._pos = (x, y)


        def __repr__(self) -> str:
            return '%s(color:%i, x:%i, y:%i)' % (
                self.getName(), self._color, *self._pos)

        def __str__(self) -> str:
            return self.__repr__()

        
        def getName(self) -> str:
            return self.__class__.__name__


        def getColor(self) -> int:
            return self._color

        
        def getPos(self) -> tuple:
            return self._pos

        def setPos(self, x: int, y: int) -> None:
            self._moved = True
            self._pos = [x, y]

        def getRect(self) -> pygame.Rect:
            rect = self.piecepng.get_rect(topleft = ((self._pos[0] + 0.01)*64, self._pos[1]*64))
            return rect

    class NullPiece(BasePiece):
        def __init__(self, _color: int, x: int, y: int) -> None:
            super().__init__(_color, x, y)
            if _color == -1:
                self.piecepng = pygame.transform.scale(pygame.image.load("src/cpb/b_pawn_png_shadow_128px.png"), (64, 64))
            else:
                self.piecepng = pygame.transform.scale(pygame.image.load("src/cpw/w_pawn_png_shadow_128px.png"), (64, 64))
    
    
        def draw(self, screen):
            self.rect = self.piecepng.get_rect(topleft = ((self._pos[0] + 0.01)*64, self._pos[1]*64))
            pygame.draw.rect(screen, (255, 0, 0), self.rect, 1)        


    class Pawn(BasePiece):
        def __init__(self, _color: int, x: int, y: int) -> None:
            super().__init__(_color, x, y)
            if _color == -1:
                self.piecepng = pygame.transform.scale(pygame.image.load("src/cpb/b_pawn_png_shadow_128px.png"), (64, 64))
                self.piecepng.convert()
            else:
                self.piecepng = pygame.transform.scale(pygame.image.load("src/cpw/w_pawn_png_shadow_128px.png"), (64, 64))
                self.piecepng.convert()

        def legalMove(self, x: int, y: int) -> bool:
            if self._pos[0]-x != 0:
                return False
                
            return int((self._pos[1]-y) * self._color) in [i+1 for i in range(1 if self._moved else 2)]

        

        def layPattern(self, x: int, y: int) -> list:
            pattern = []
            if not self._moved and abs(y-self._pos[1]) == 2: # check if the piece is moved and the destination consists of 2 y movements
                pattern.append([self._pos[0], self._pos[1]+(1*self._color)])
            return pattern

        def draw(self, screen):
            screen.blit(self.piecepng, ((self._pos[0] + 0.01)*64, self._pos[1]*64))
            self.rect = self.piecepng.get_rect(topleft = ((self._pos[0] + 0.01)*64, self._pos[1]*64))
            pygame.draw.rect(screen, (255, 0, 0), self.rect, 1)
            

    class Knight(BasePiece):
        def __init__(self, _color: int, x: int, y: int) -> None:
            super().__init__(_color, x, y)
            if _color == -1:
                self.piecepng = pygame.transform.scale(pygame.image.load("src/cpb/b_knight_png_shadow_128px.png"), (64, 64))
            else:
                self.piecepng = pygame.transform.scale(pygame.image.load("src/cpw/w_knight_png_shadow_128px.png"), (64, 64))
            

        def legalMove(self, x: int, y: int) -> bool:
            return sorted([abs(self._pos[0]-x), abs(self._pos[1]-y)]) == [1, 2]


        def draw(self, screen):
            screen.blit(self.piecepng, ((self._pos[0] + 0.01)*64, self._pos[1]*64))
            self.rect = self.piecepng.get_rect(topleft = ((self._pos[0] + 0.01)*64, self._pos[1]*64))
            pygame.draw.rect(screen, (255, 0, 0), self.rect, 1)
            
        
    class Bishop(BasePiece):
        def __init__(self, _color: int, x: int, y: int) -> None:
            super().__init__(_color, x, y)
            if _color == -1:
                self.piecepng = pygame.transform.scale(pygame.image.load("src/cpb/b_bishop_png_shadow_128px.png"), (64, 64))
            else:
                self.piecepng = pygame.transform.scale(pygame.image.load("src/cpw/w_bishop_png_shadow_128px.png"), (64, 64))
            

        def legalMove(self, x: int, y: int) -> bool:
            return abs(self._pos[0]-x) == abs(self._pos[1]-y)
        

        def layPattern(self, x: int, y: int) -> list:
            pattern = []
            
            x_dir = 1 if x-self._pos[0] > 0 else -1
            y_dir = 1 if y-self._pos[1] > 0 else -1

            for i in range(1, abs(self._pos[1]-y)+1):
                pattern.append([
                    self._pos[0] + (x_dir*i),
                    self._pos[1] + (y_dir*i)
                ])
            
            return pattern

        def draw(self, screen):
            screen.blit(self.piecepng, ((self._pos[0] + 0.01)*64, self._pos[1]*64))
            self.rect = self.piecepng.get_rect(topleft = ((self._pos[0] + 0.01)*64, self._pos[1]*64))
            pygame.draw.rect(screen, (255, 0, 0), self.rect, 1)
            

    class Rook(BasePiece):
        def __init__(self, _color: int, x: int, y: int) -> None:
            super().__init__(_color, x, y)
            if _color == -1:
                self.piecepng = pygame.transform.scale(pygame.image.load("src/cpb/b_rook_png_shadow_128px.png"), (64, 64))
            else:
                self.piecepng = pygame.transform.scale(pygame.image.load("src/cpw/w_rook_png_shadow_128px.png"), (64, 64))

        def legalMove(self, x: int, y: int) -> bool:
            return (self._pos[0] != x and self._pos[1] == y) or (self._pos[0] == x and self._pos[1] != y)
        

        def layPattern(self, x: int, y: int) -> list:
            pattern = []
            
            if x != self._pos[0] and self._pos[1] == y:
                diff = 1 if x-self._pos[0] > 0 else -1

                for i in range(1, abs(self._pos[0]-x)):
                    pattern.append([self._pos[0] + (diff*i), y])

            elif x == self._pos[0] and self._pos[1] != y:
                diff = 1 if y-self._pos[1] > 0 else -1

                for i in range(1, abs(self._pos[1]-y)):
                    pattern.append([x, self._pos[1] + (diff*i)])

        def draw(self, screen):
            screen.blit(self.piecepng, ((self._pos[0] + 0.01)*64, self._pos[1]*64))
            self.rect = self.piecepng.get_rect(topleft = ((self._pos[0] + 0.01)*64, self._pos[1]*64))
            pygame.draw.rect(screen, (255, 0, 0), self.rect, 1)
            
        
    class Queen(BasePiece):
        def __init__(self, _color: int, x: int, y: int) -> None:
            super().__init__(_color, x, y)
            if _color == -1:
                self.piecepng = pygame.transform.scale(pygame.image.load("src/cpb/b_queen_png_shadow_128px.png"), (64, 64))
            else:
                self.piecepng = pygame.transform.scale(pygame.image.load("src/cpw/w_queen_png_shadow_128px.png"), (64, 64))
            

        def legalMove(self, x: int, y: int) -> bool:
            return Piece.Rook.legalMove(self, x, y) or Piece.Bishop.legalMove(self, x, y)
        

        def layPattern(self, x: int, y: int) -> list:
            pattern = []
            if Piece.Rook.legalMove(self, x, y):
                pattern = Piece.Rook.layPattern(self, x, y)
            elif Piece.Bishop.legalMove(self, x, y):
                pattern = Piece.Bishop.layPattern(self, x, y)
            return pattern

        def draw(self, screen):
            screen.blit(self.piecepng, ((self._pos[0] + 0.01)*64, self._pos[1]*64))
            self.rect = self.piecepng.get_rect(topleft = ((self._pos[0] + 0.01)*64, self._pos[1]*64))
            pygame.draw.rect(screen, (255, 0, 0), self.rect, 1)
            

    class King(BasePiece):
        def __init__(self, _color: int, x: int, y: int) -> None:
            super().__init__(_color, x, y)
            if _color == -1:
                self.piecepng = pygame.transform.scale(pygame.image.load("src/cpb/b_king_png_shadow_128px.png"), (64, 64))
            else:
                self.piecepng = pygame.transform.scale(pygame.image.load("src/cpw/w_king_png_shadow_128px.png"), (64, 64))
            

        def legalMove(self, x: int, y: int) -> bool:
            return abs(self._pos[0]-x) in range(2) and abs(self._pos[1]-y) in range(2)


        def draw(self, screen):
            screen.blit(self.piecepng, ((self._pos[0] + 0.01)*64, self._pos[1]*64))
            self.rect = self.piecepng.get_rect(topleft = ((self._pos[0] + 0.01)*64, self._pos[1]*64))
            pygame.draw.rect(screen, (255, 0, 0), self.rect, 1)
            