from main import posted

reacted = False

FEN = None
turn = None
FENCHANGE = []
PAWNS = [0] * 64
KNIGHTS = [0] * 64
BISHOPS = [0] * 64
ROOKS = [0] * 64 
KINGS = [0] * 64
QUEENS = [0] * 64
UNIONNOK = [0] * 64
UNIONK = [0] * 64
legalMoves = []
tempvar = 0
eval = 0
modified_string = ''.join([char for char in FEN])
import re
import os
def conversion():
  global modified_string
  for char in modified_string:
      FENCHANGE.append(char)
  modified_string= re.sub(r'(\d+)', lambda match: 'l' * int(match.group()), modified_string)
  modified_string = modified_string.replace('/', '')
  FENCHANGE.clear()
  for char in modified_string:
    if not char.isnumeric() and char != 'l':
      FENCHANGE.append(char)
    elif char == 'l':
      FENCHANGE.append(0)
  for index, item in enumerate(FENCHANGE):
        if item == 'r':
            ROOKS[index] = -5
            UNIONNOK[index] = -5
            UNIONK[index] = -5
        elif item == 'R':
            ROOKS[index] = 5
            UNIONNOK[index] = 5
            UNIONK[index] = 5
        elif item == 'n':
            KNIGHTS[index] = -3
            UNIONNOK[index] = -3
            UNIONK[index] = -3
        elif item == 'N':
            KNIGHTS[index] = 3
            UNIONNOK[index] = 3
            UNIONK[index] = 3
        elif item == 'b':
            BISHOPS[index] = -4
            UNIONNOK[index] = -4
            UNIONK[index] = -4
        elif item == 'B':
            BISHOPS[index] = 4
            UNIONNOK[index] = 4
            UNIONK[index] = 4
        elif item == 'p':
            PAWNS[index] = -1
            UNIONNOK[index] = -1
            UNIONK[index] = -1
        elif item == 'P':
            PAWNS[index] = 1
            UNIONNOK[index] = 1
            UNIONK[index] = 1
        elif item == 'k':
            KINGS[index] = -127
            UNIONK[index] = -127
        elif item == 'K':
            KINGS[index] = 127 
            UNIONK[index] = 127
        elif item == 'q':
            QUEENS[index] = -9
            UNIONNOK[index] = -9
            UNIONK[index] = -9
        elif item == 'Q':
            QUEENS[index] = 9
            UNIONNOK[index] = 9
            UNIONK[index] = 9


def empty_black(squarenum):
  if UNIONK[squarenum] < 0:
    return True
  else:
    return False
def empty_white(squarenum):
  if UNIONK[squarenum] > 0:
    return True
  else:
    return False

def findLegal():
  for i in PAWNS :
    if turn == 'w':
      if i > 0:
        if empty_black(i+8) == True:
          legalMoves.append('P'+str(i+8))
        if i-7 > 0 and empty_black(i+7) == False:
          legalMoves.append('P'+str(i+8))
        if i-9 > 0 and empty_black(i+9) == False and i % 8 != 1:
          legalMoves.append('P'+str(i+9))
    elif turn == 'b':
      if i < 0:
        if empty_white(i+8) == True:
          legalMoves.append('P'+str(i+8))
        if i+7 < 64 and empty_white(i+7) == False: 
          legalMoves.append('p'+str(i+7))
        if i+9 < 64 and empty_white(i+9) == False and i %8 != 1: 
          legalMoves.append('p'+str(i+9))


def evaluate():
    for u in range(len(UNIONNOK)):
      global eval
      eval = eval + UNIONNOK[u]
conversion() 
findLegal() 
evaluate()
# print(eval)
# print(legalMoves)

print("CONNECTION FROM: ", str(addr))

while not posted:
	###
	pass
else:
	reacted = True