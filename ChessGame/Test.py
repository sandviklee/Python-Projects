import re

txt = open("src/chessboard.txt", "r")

lst = []
lst2 = []

for text in txt:
    for word in text:
        if re.search("[a-zA-Z]", word):
            lst2.append(word)
        elif word == "0":
            lst2.append("0")
        elif (word == "\n"):
            lst.append(lst2)
            lst2 = []
lst.append(lst2)

print(lst)