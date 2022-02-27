# import re
import pygame
from Pieces import Piece

# txt = open("src/chessboard.txt", "r")

# lst = []
# lst2 = []

# for text in txt:
#     for word in text:
#         if re.search("[a-zA-Z]", word):
#             lst2.append(word)
#         elif word == "0":
#             lst2.append("0")
#         elif (word == "\n"):
#             lst.append(lst2)
#             lst2 = []
# lst.append(lst2)

# print(lst)



field = []
back_line = ['Rook', 'Knight', 'Bishop', 'Queen', 'King', 'Bishop', 'Knight', 'Rook']

for c in [-1, 1]:
    for x in range(8):
        field.append(Piece.Pawn(c, x, (6 if c > 0 else 1)))
    for x, Piece in enumerate([getattr(Piece, p) for p in back_line]):
        field.append(Piece(c, x, (7 if c > 0 else 0)))