import re
import math
listp= [0, 0, 0, 0, 0, 0, 0, 0,
        -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5,
        -0.1, -0.1, -0.2, -0.3, -0.3, -0.2, -0.1, -0.1,
        -0.5, -0.5, -0.10, -0.25, -0.25, -0.10, -0.5, -0.5,
        0, 0, 0, -0.2, -0.2, 0, 0, 0,
        0.5, 0.5, 0.1, 0, 0, 0.1, 0.5, 0.5,
        0.5, 0.1, 0.1, 0.2, 0.2, 0.1, 0.1, 0.5,
        0, 0, 0, 0, 0, 0, 0, 0]
listn=[-0.5, -0.4, -0.3, -0.3, -0.3, -0.3, -0.4, -0.5,
      -0.4, -0.2, 0, 0.3, 0.3, 0, -0.2, -0.4,
      -0.3, 0, 0.6, 0.9, 0.9, 0.6, 0, -0.3,
      -0.3, 0.3, 0.9, 1.2, 1.2, 0.9, 0.3, -0.3,
      -0.3, 0.3, 0.9, 1.2, 1.2, 0.9, 0.3, -0.3,
      -0.3, 0, 0.6, 0.9, 0.9, 0.6, 0, -0.3,
      -0.4, -0.2, 0, 0.3, 0.3, 0, -0.2, -0.4,
      -0.5, -0.4, -0.3, -0.3, -0.3, -0.3, -0.4, -0.5]
listb= [
-0.2, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.2,
-0.1, 0, 0, 0, 0, 0, 0, -0.1,
-0.1, 0, 0.3, 0.3, 0.3, 0.3, 0, -0.1,
-0.1, 0.3, 0.3, 0.6, 0.6, 0.3, 0.3, -0.1,
-0.1, 0, 0.3, 0.6, 0.6, 0.3, 0, -0.1,
-0.1, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, -0.1,
-0.1, 0, 0.3, 0, 0, 0.3, 0, -0.1,
-0.2, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.2] 
listr= [0, 0, 0, 0.3, 0.3, 0, 0, 0,
       -0.1, 0, 0, 0, 0, 0, 0, -0.1,
       -0.1, 0, 0, 0, 0, 0, 0, -0.1,
       -0.1, 0, 0, 0, 0, 0, 0, -0.1,
       -0.1, 0, 0, 0, 0, 0, 0, -0.1,
       -0.1, 0, 0, 0, 0, 0, 0, -0.1,
       0.3, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.3,
       0, 0, 0, 0, 0, 0, 0, 0]
listq=[-0.1, -0.1, -0.1, 0, 0, -0.1, -0.1, -0.1,
      -0.1, 0, 0, 0, 0, 0, 0, -0.1,
      -0.1, 0, 0.3, 0.3, 0.3, 0.3, 0, -0.1,
      0, 0, 0.3, 0.6, 0.6, 0.3, 0, -0.1,
      0, 0, 0.3, 0.6, 0.6, 0.3, 0, -0.1,
      -0.1, 0, 0.3, 0.3, 0.3, 0.3, 0, -0.1,
      -0.1, 0, 0, 0, 0, 0, 0, -0.1,
      -0.1, -0.1, -0.1, 0, 0, -0.1, -0.1, -0.1]
listk=  [0.3, 0.2, 0.2, 0.1, 0.1, 0.2, 0.2, 0.3,
       0.3, 0.2, 0.2, 0.1, 0.1, 0.2, 0.2, 0.3,
       0.3, 0.2, 0.2, 0.1, 0.1, 0.2, 0.2, 0.3,
       0.3, 0.2, 0.2, 0.1, 0.1, 0.2, 0.2, 0.3,
       0.3, 0.2, 0.2, 0.1, 0.1, 0.2, 0.2, 0.3,
       0.3, 0.2, 0.2, 0.1, 0.1, 0.2, 0.2, 0.3,
       0.3, 0.2, 0.2, 0.1, 0.1, 0.2, 0.2, 0.3,
       0.3, 0.2, 0.2, 0.1, 0.1, 0.2, 0.2, 0.3]
global UNIONK
global PAWNS
global KNIGHTS
global BISHOPS
global ROOKS
global KINGS
global QUEENS
global UNIONNOK
FENCHANGE = []
PAWNS = [0] * 64
KNIGHTS = [0] * 64
BISHOPS = [0] * 64
ROOKS = [0] * 64 
KINGS = [0] * 64
QUEENS = [0] * 64
UNIONNOK = [0] * 64
UNIONK = [0] * 64
tempvar = 0
eval = 0
def empty_black(squarenum):
  if UNIONK[squarenum] < 0:
    return False
  else:
    return True
def empty_white(squarenum):
  if UNIONK[squarenum] > 0:
    return False
  else:
    return True
def empty(squarenum):
  if UNIONK[squarenum] != 0:
    return False
  else:
    return True
def current_row(squarenum):
  return (int(squarenum)//8)+1
def squarecolor(squarenum):
  return (int(squarenum) % 2)
def current_column(squarenum):
  return (int(squarenum) % 8)
def convert(inputFEN):
  PAWNS = [0] * 64
  KNIGHTS = [0] * 64
  BISHOPS = [0] * 64
  ROOKS = [0] * 64 
  KINGS = [0] * 64
  QUEENS = [0] * 64
  UNIONNOK = [0] * 64
  UNIONK = [0] * 64
  modified_string = ''.join([char for char in inputFEN])
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
            KINGS[index] = -10
            UNIONK[index] = -10
        elif item == 'K':
            KINGS[index] = 10
            UNIONK[index] = 10
        elif item == 'q':
            QUEENS[index] = -9
            UNIONNOK[index] = -9
            UNIONK[index] = -9
        elif item == 'Q':
            QUEENS[index] = 9
            UNIONNOK[index] = 9
            UNIONK[index] = 9
def returnconvert(inputFEN):
          UNIONK = [0] * 64
          modified_string = ''.join([char for char in inputFEN])
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
                    UNIONK[index] = -5
                elif item == 'R':
                    UNIONK[index] = 5
                elif item == 'n':
                    UNIONK[index] = -3
                elif item == 'N':
                    UNIONK[index] = 3
                elif item == 'b':
                    UNIONK[index] = -4
                elif item == 'B':
                    UNIONK[index] = 4
                elif item == 'p':
                    UNIONK[index] = -1
                elif item == 'P':
                    UNIONK[index] = 1
                elif item == 'k':
                    UNIONK[index] = -10
                elif item == 'K':
                    UNIONK[index] = 10
                elif item == 'q':
                    UNIONK[index] = -9
                elif item == 'Q':
                    UNIONK[index] = 9
          return UNIONK
def findLegal(inputFEN, turntype): 
  legalMoves = []
  modified_string = ''.join([char for char in inputFEN])
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
            KINGS[index] = -10
            UNIONK[index] = -10
        elif item == 'K':
            KINGS[index] = 10
            UNIONK[index] = 10
        elif item == 'q':
            QUEENS[index] = -9
            UNIONNOK[index] = -9
            UNIONK[index] = -9
        elif item == 'Q':
            QUEENS[index] = 9
            UNIONNOK[index] = 9
            UNIONK[index] = 9
  for i in range(0, len(PAWNS)-1, 1): 
    if turntype == 'w':
      if PAWNS[i] > 0:
        if i-8>0 and empty(i-8):
          legalMoves.append('P'+str(i+1)+'P'+str(i-7))
        if i-7 > 0 and not empty_black(i-7) and i%8 != 0:
          legalMoves.append('P'+str(i+1)+'P'+str(i-6))
        if i-9 > 0 and not empty_black(i-9) and i % 8 != 1:
          legalMoves.append('P'+str(i+1)+'P'+str(i-8))
        if i//8 == 6 and empty(i-8) and empty(i-16):
          legalMoves.append('P'+str(i+1)+'P'+str(i-15))
    elif turntype == 'b':
      if PAWNS[i] < 0:
        if i+8<64 and empty(i+8):
          legalMoves.append('p'+str(i+1)+'p'+str(i+9))
        if i+7 < 64 and not empty_white(i+7) and i%8 != 1: 
          legalMoves.append('p'+str(i+1)+'p'+str(i+8))
        if i+9 < 64 and not empty_white(i+9) and i %8 != 0: 
          legalMoves.append('p'+str(i+1)+'p'+str(i+10))
        if i//8 == 1 and empty(i+8) and empty(i+16):
          legalMoves.append('p'+str(i+1)+'p'+str(i+17))
  for i in range(len(KNIGHTS)):
    file_i = i % 8  
    if turntype == 'w':
      if KNIGHTS[i] > 0:
        possible_moves = [
          i - 17, i - 15, i - 10, i - 6, i + 6, i + 10, i + 15, i + 17
        ]
        legalMoves.extend(['N'+str(i+1)+'N' + str(move+1) for move in possible_moves if 0 < move < 64 and empty_white(move) and abs(move % 8 - file_i) <= 2])

    elif turntype == 'b':
      if KNIGHTS[i] < 0:
        possible_moves = [
          i - 17, i - 15, i - 10, i - 6, i + 6, i + 10, i + 15, i + 17
         ]
        legalMoves.extend(['n'+str(i+1)+'n' + str(move+1) for move in possible_moves if 0 < move < 64 and empty_black(move) and abs(move % 8 - file_i) <= 2])
  for i in range(len(BISHOPS)):
    if turntype == 'w' and BISHOPS[i] > 0:
      possible_moves_1 = [i+7, i+14, i+21, i+28, i+35, i+42, i+49, i+56, i+63]
      possible_moves_2 = [i-7, i-14, i-21, i-28, i-35, i-42, i-49, i-56, i-63]
      possible_moves_3= [i+9, i+18, i+27, i+36, i+45, i+54, i+63]
      possible_moves_4 = [i-9, i-18, i-27, i-36, i-45, i-54, i-63]
      possible_moves_1 = possible_moves_1[:8-(i%8)]
      possible_moves_2 = possible_moves_2[:(i%8)]
      possible_moves_3 = possible_moves_3[:8-(i%8)]
      possible_moves_1 = possible_moves_1[:(i%8)]
      for index, j in enumerate(possible_moves_1):
        if 0<j<64:
          if empty_white(j) and empty_black(j) and j%8 != 0:
            pass
          else:
           if not empty_white(j): 
            possible_moves_1 = possible_moves_1[:index]
            break
           elif not empty_black(j) or j%8 == 0:
            possible_moves_1 = possible_moves_1[:index+1]
            break

      for index, j in enumerate(possible_moves_2):
        if 0<j<64:
          if empty_white(j) and empty_black(j) and j%8 != 0:
            pass
          else:
           if not empty_white(j): 
            possible_moves_2 = possible_moves_2[:index]
            break
           elif not empty_black(j) or j%8 == 0:
            possible_moves_2 = possible_moves_2[:index+1]
            break
      for index, j in enumerate(possible_moves_3):
        if 0<j<64:
          if empty_white(j) and empty_black(j) and j%8 != 0:
            pass
          else:
           if not empty_white(j): 
            possible_moves_3 = possible_moves_3[:index]
            break
           elif not empty_black(j) or j%8 == 0:
            possible_moves_3 = possible_moves_3[:index+1]
            break
      for index, j in enumerate(possible_moves_4):
        if 0<j<64:
          if empty_white(j) and empty_black(j) and j%8 != 0:
            pass
          else:
           if not empty_white(j): 
            possible_moves_4 = possible_moves_4[:index]
            break
           elif not empty_black(j) or j%8 == 0:
            possible_moves_4 = possible_moves_4[:index+1]
            break
      legalMoves.extend(['B'+str(i+1)+'B' + str(move+1) for move in possible_moves_1 if 0<move<64])
      legalMoves.extend(['B'+str(i+1)+'B' + str(move+1) for move in possible_moves_2 if 0<move<64])
      legalMoves.extend(['B'+str(i+1)+'B' + str(move+1) for move in possible_moves_3 if 0<move<64])
      legalMoves.extend(['B'+str(i+1)+'B' + str(move+1) for move in possible_moves_4 if 0<move<64])
    if turntype == 'b' and BISHOPS[i] < 0:
            possible_moves_1 = [i+7, i+14, i+21, i+28, i+35, i+42, i+49, i+56, i+63]
            possible_moves_2 = [i-7, i-14, i-21, i-28, i-35, i-42, i-49, i-56, i-63]
            possible_moves_3= [i+9, i+18, i+27, i+36, i+45, i+54, i+63]
            possible_moves_4 = [i-9, i-18, i-27, i-36, i-45, i-54, i-63]
            possible_moves_1 = possible_moves_1[:8-(i%8)]
            possible_moves_2 = possible_moves_2[:(i%8)]
            possible_moves_3 = possible_moves_3[:8-(i%8)]
            possible_moves_1 = possible_moves_1[:(i%8)]
            for index, j in enumerate(possible_moves_1):
              if 0<j<64:
                if empty_white(j) and empty_black(j) and j%8 !=0:
                  pass
                else:
                 if not empty_black(j): 
                  possible_moves_1 = possible_moves_1[:index]
                  break
                 elif not empty_white(j) or j%8 == 0:
                  possible_moves_1 = possible_moves_1[:index+1]
                  break
            for index, j in enumerate(possible_moves_2):
              if 0<j<64:
                if empty_white(j) and empty_black(j) and j%8 !=0:
                  pass
                else:
                 if not empty_black(j): 
                  possible_moves_2 = possible_moves_2[:index]
                  break
                 elif not empty_white(j) or j%8 ==0:
                  possible_moves_2 = possible_moves_2[:index+1]
                  break
            for index, j in enumerate(possible_moves_3):
              if 0<j<64:
                if empty_white(j) and empty_black(j) and j%8 !=0:
                  pass
                else:
                 if not empty_black(j): 
                  possible_moves_3 = possible_moves_3[:index]
                  break
                 elif not empty_white(j) or j%8 == 0:
                  possible_moves_3 = possible_moves_3[:index+1]
                  break
            for index, j in enumerate(possible_moves_4):
              if 0<j<64:
                if empty_white(j) and empty_black(j) and j%8 !=0:
                  pass
                else:
                 if not empty_black(j): 
                  possible_moves_4 = possible_moves_4[:index]
                  break
                 elif not empty_white(j) or j%8 == 0:
                  possible_moves_4 = possible_moves_4[:index+1]
                  break
            legalMoves.extend(['b'+str(i+1)+'b' + str(move+1) for move in possible_moves_1 if 0<move<64])
            legalMoves.extend(['b'+str(i+1)+'b' + str(move+1) for move in possible_moves_2 if 0<move<64])
            legalMoves.extend(['b'+str(i+1)+'b' + str(move+1) for move in possible_moves_3 if 0<move<64])
            legalMoves.extend(['b'+str(i+1)+'b' + str(move+1) for move in possible_moves_4 if 0<move<64])
  for i in range(len(ROOKS)):
    if turntype == 'w' and ROOKS[i] > 0:
      possible_moves_1 = [i+1, i+2, i+3, i+4, i+5, i+6, i+7]
      possible_moves_2 = [i-1, i-2, i-3, i-4, i-5, i-6, i-7]
      possible_moves_3 = [i+8, i+16, i+24, i+32, i+40, i+48, i+56]
      possible_moves_4 = [i-8, i-16, i-24, i-32, i-40, i-48, i-56]
      for index, j in enumerate(possible_moves_1):
        if 0<j<64:
          if empty_white(j) and current_row(i) == current_row(j) and empty_black(j):
            pass
          else:
            if not empty_white(j):
              possible_moves_1 = possible_moves_1[:index]
              break
            if not empty_black(j):
              possible_moves_1 = possible_moves_1[:index+1]
      for index, j in enumerate(possible_moves_2):
        if 0<j<64:
          if empty_white(j) and current_row(i) == current_row(j) and empty_black(j):
            pass
          else:
            if not empty_white(j):
              possible_moves_2 = possible_moves_2[:index]
              break
            if not empty_black(j):
              possible_moves_2 = possible_moves_2[:index+1]
      for index, j in enumerate(possible_moves_3):
        if 0<j<64:
          if empty_white(j) and current_row(i) == current_row(j) and empty_black(j):
            pass
          else:
            if not empty_white(j):
              possible_moves_3 = possible_moves_3[:index]
              break
            if not empty_black(j):
              possible_moves_3 = possible_moves_3[:index+1]
      for index, j in enumerate(possible_moves_4):
        if 0<j<64:
          if empty_white(j) and current_row(i) == current_row(j) and empty_black(j):
            pass
          else:
            if not empty_white(j):
              possible_moves_4 = possible_moves_4[:index]
              break
            if not empty_black(j):
              possible_moves_4 = possible_moves_4[:index+1]

      legalMoves.extend(['R'+str(i+1)+'R' + str(move+1) for move in possible_moves_1 if 0<move<64])
      legalMoves.extend(['R'+str(i+1)+'R' + str(move+1) for move in possible_moves_2 if 0<move<64])
      legalMoves.extend(['R'+str(i+1)+'R' + str(move+1) for move in possible_moves_3 if 0<move<64])
      legalMoves.extend(['R'+str(i+1)+'R' + str(move+1) for move in possible_moves_4 if 0<move<64])
    if turntype == 'b' and ROOKS[i] < 0:
        possible_moves_1 = [i+1, i+2, i+3, i+4, i+5, i+6, i+7]
        possible_moves_2 = [i-1, i-2, i-3, i-4, i-5, i-6, i-7]
        possible_moves_3 = [i+8, i+16, i+24, i+32, i+40, i+48, i+56]
        possible_moves_4 = [i-8, i-16, i-24, i-32, i-40, i-48, i-56]
        for index, j in enumerate(possible_moves_1):
          if 0<j<64:
            if empty_white(j) and current_row(i) == current_row(j) and empty_black(j):
              pass
            else:
              if not empty_black(j):
                possible_moves_1 = possible_moves_1[:index]
                break
              if not empty_white(j):
                possible_moves_1 = possible_moves_1[:index+1]
        for index, j in enumerate(possible_moves_2):
          if 0<j<64:
            if empty_white(j) and current_row(i) == current_row(j) and empty_black(j):
              pass
            else:
              if not empty_black(j):
                possible_moves_2 = possible_moves_2[:index]
                break
              if not empty_white(j):
                possible_moves_2 = possible_moves_2[:index+1]
        for index, j in enumerate(possible_moves_3):
          if 0<j<64:
            if empty_white(j) and current_row(i) == current_row(j) and empty_black(j):
              pass
            else:
              if not empty_black(j):
                possible_moves_3 = possible_moves_3[:index]
                break
              if not empty_white(j):
                possible_moves_3 = possible_moves_3[:index+1]
        for index, j in enumerate(possible_moves_4):
          if 0<j<64:
            if empty_white(j) and current_row(i) == current_row(j) and empty_black(j):
              pass
            else:
              if not empty_black(j):
                possible_moves_4 = possible_moves_4[:index]
                break
              if not empty_white(j):
                possible_moves_4 = possible_moves_4[:index+1]

        legalMoves.extend(['r'+str(i+1)+'r' + str(move+1) for move in possible_moves_1 if 0<move<64])
        legalMoves.extend(['r'+str(i+1)+'r' + str(move+1) for move in possible_moves_2 if 0<move<64])
        legalMoves.extend(['r'+str(i+1)+'r' + str(move+1) for move in possible_moves_3 if 0<move<64])
        legalMoves.extend(['r'+str(i+1)+'r' + str(move+1) for move in possible_moves_4 if 0<move<64])
  for i in range(len(QUEENS)):
    if turntype == 'w' and QUEENS[i] > 0:
      possible_moves_1 = [i+7, i+14, i+21, i+28, i+35, i+42, i+49, i+56, i+63]
      possible_moves_2 = [i-7, i-14, i-21, i-28, i-35, i-42, i-49, i-56, i-63]
      possible_moves_3= [i+9, i+18, i+27, i+36, i+45, i+54, i+63]
      possible_moves_4 = [i-9, i-18, i-27, i-36, i-45, i-54, i-63]
      possible_moves_1 = possible_moves_1[:8-(i%8)]
      possible_moves_2 = possible_moves_2[:(i%8)]
      possible_moves_3 = possible_moves_3[:8-(i%8)]
      possible_moves_1 = possible_moves_1[:(i%8)]
      for index, j in enumerate(possible_moves_1):
        if 0<j<64:
          if empty_white(j) and empty_black(j) and j%8 != 0:
            pass
          else:
           if not empty_white(j): 
            possible_moves_1 = possible_moves_1[:index]
            break
           elif not empty_black(j) or j%8 == 0:
            possible_moves_1 = possible_moves_1[:index+1]
            break

      for index, j in enumerate(possible_moves_2):
        if 0<j<64:
          if empty_white(j) and empty_black(j) and j%8 != 0:
            pass
          else:
           if not empty_white(j): 
            possible_moves_2 = possible_moves_2[:index]
            break
           elif not empty_black(j) or j%8 == 0:
            possible_moves_2 = possible_moves_2[:index+1]
            break
      for index, j in enumerate(possible_moves_3):
        if 0<j<64:
          if empty_white(j) and empty_black(j) and j%8 != 0:
            pass
          else:
           if not empty_white(j):
            possible_moves_3 = possible_moves_3[:index]
            break
           elif not empty_black(j) or j%8 == 0:
            possible_moves_3 = possible_moves_3[:index+1]
            break
      for index, j in enumerate(possible_moves_4):
        if 0<j<64:
          if empty_white(j) and empty_black(j) and j%8 != 0:
            pass
          else:
           if not empty_white(j): 
            possible_moves_4 = possible_moves_4[:index]
            break
           elif not empty_black(j) or j%8 == 0:
            possible_moves_4 = possible_moves_4[:index+1]
            break
      legalMoves.extend(['Q'+str(i+1)+'Q' + str(move+1) for move in possible_moves_1 if 0<move<64])
      legalMoves.extend(['Q'+str(i+1)+'Q' + str(move+1) for move in possible_moves_2 if 0<move<64])
      legalMoves.extend(['Q'+str(i+1)+'Q' + str(move+1) for move in possible_moves_3 if 0<move<64])
      legalMoves.extend(['Q'+str(i+1)+'Q' + str(move+1) for move in possible_moves_4 if 0<move<64])
      possible_moves_1 = [i+1, i+2, i+3, i+4, i+5, i+6, i+7]
      possible_moves_2 = [i-1, i-2, i-3, i-4, i-5, i-6, i-7]
      possible_moves_3 = [i+8, i+16, i+24, i+32, i+40, i+48, i+56]
      possible_moves_4 = [i-8, i-16, i-24, i-32, i-40, i-48, i-56]
      for index, j in enumerate(possible_moves_1):
        if 0<j<64:
          if empty_white(j) and current_row(i) == current_row(j) and empty_black(j):
            pass
          else:
            if not empty_white(j):
              possible_moves_1 = possible_moves_1[:index]
              break
            if not empty_black(j):
              possible_moves_1 = possible_moves_1[:index+1]
      for index, j in enumerate(possible_moves_2):
        if 0<j<64:
          if empty_white(j) and current_row(i) == current_row(j) and empty_black(j):
            pass
          else:
            if not empty_white(j):
              possible_moves_2 = possible_moves_2[:index]
              break
            if not empty_black(j):
              possible_moves_2 = possible_moves_2[:index+1]
      for index, j in enumerate(possible_moves_3):
        if 0<j<64:
          if empty_white(j) and current_row(i) == current_row(j) and empty_black(j):
            pass
          else:
            if not empty_white(j):
              possible_moves_3 = possible_moves_3[:index]
              break
            if not empty_black(j):
              possible_moves_3 = possible_moves_3[:index+1]
      for index, j in enumerate(possible_moves_4):
        if 0<j<64:
          if empty_white(j) and current_row(i) == current_row(j) and empty_black(j):
            pass
          else:
            if not empty_white(j):
              possible_moves_4 = possible_moves_4[:index]
              break
            if not empty_black(j):
              possible_moves_4 = possible_moves_4[:index+1]

      legalMoves.extend(['Q'+str(i+1)+'Q' + str(move+1) for move in possible_moves_1 if 0<move<64])
      legalMoves.extend(['Q'+str(i+1)+'Q' + str(move+1) for move in possible_moves_2 if 0<move<64])
      legalMoves.extend(['Q'+str(i+1)+'Q' + str(move+1) for move in possible_moves_3 if 0<move<64])
      legalMoves.extend(['Q'+str(i+1)+'Q' + str(move+1) for move in possible_moves_4 if 0<move<64])
    if turntype == 'b' and QUEENS[i] < 0:
      possible_moves_1 = [i+7, i+14, i+21, i+28, i+35, i+42, i+49, i+56, i+63]
      possible_moves_2 = [i-7, i-14, i-21, i-28, i-35, i-42, i-49, i-56, i-63]
      possible_moves_3= [i+9, i+18, i+27, i+36, i+45, i+54, i+63]
      possible_moves_4 = [i-9, i-18, i-27, i-36, i-45, i-54, i-63]
      possible_moves_1 = possible_moves_1[:8-(i%8)]
      possible_moves_2 = possible_moves_2[:(i%8)]
      possible_moves_3 = possible_moves_3[:8-(i%8)]
      possible_moves_1 = possible_moves_1[:(i%8)]
      for index, j in enumerate(possible_moves_1):
        if 0<j<64:
          if empty_white(j) and empty_black(j) and j%8 !=0:
            pass
          else:
           if not empty_black(j): 
            possible_moves_1 = possible_moves_1[:index]
            break
           elif not empty_white(j) or j%8 == 0:
            possible_moves_1 = possible_moves_1[:index+1]
            break
      for index, j in enumerate(possible_moves_2):
        if 0<j<64:
          if empty_white(j) and empty_black(j) and j%8 !=0:
            pass
          else:
           if not empty_black(j): 
            possible_moves_2 = possible_moves_2[:index]
            break
           elif not empty_white(j) or j%8 ==0:
            possible_moves_2 = possible_moves_2[:index+1]
            break
      for index, j in enumerate(possible_moves_3):
        if 0<j<64:
          if empty_white(j) and empty_black(j) and j%8 !=0:
            pass
          else:
           if not empty_black(j): 
            possible_moves_3 = possible_moves_3[:index]
            break
           elif not empty_white(j) or j%8 == 0:
            possible_moves_3 = possible_moves_3[:index+1]
            break
      for index, j in enumerate(possible_moves_4):
        if 0<j<64:
          if empty_white(j) and empty_black(j) and j%8 !=0:
            pass
          else:
           if not empty_black(j): 
            possible_moves_4 = possible_moves_4[:index]
            break
           elif not empty_white(j) or j%8 == 0:
            possible_moves_4 = possible_moves_4[:index+1]
            break
      legalMoves.extend(['q'+str(i+1)+'q' + str(move+1) for move in possible_moves_1 if 0<move<64])
      legalMoves.extend(['q'+str(i+1)+'q' + str(move+1) for move in possible_moves_2 if 0<move<64])
      legalMoves.extend(['q'+str(i+1)+'q' + str(move+1) for move in possible_moves_3 if 0<move<64])
      legalMoves.extend(['q'+str(i+1)+'q' + str(move+1) for move in possible_moves_4 if 0<move<64])
      possible_moves_1 = [i+1, i+2, i+3, i+4, i+5, i+6, i+7]
      possible_moves_2 = [i-1, i-2, i-3, i-4, i-5, i-6, i-7]
      possible_moves_3 = [i+8, i+16, i+24, i+32, i+40, i+48, i+56]
      possible_moves_4 = [i-8, i-16, i-24, i-32, i-40, i-48, i-56]
      for index, j in enumerate(possible_moves_1):
        if 0<j<64:
          if empty_white(j) and current_row(i) == current_row(j) and empty_black(j):
            pass
          else:
            if not empty_black(j):
              possible_moves_1 = possible_moves_1[:index]
              break
            if not empty_white(j):
              possible_moves_1 = possible_moves_1[:index+1]
      for index, j in enumerate(possible_moves_2):
        if 0<j<64:
          if empty_white(j) and current_row(i) == current_row(j) and empty_black(j):
            pass
          else:
            if not empty_black(j):
              possible_moves_2 = possible_moves_2[:index]
              break
            if not empty_white(j):
              possible_moves_2 = possible_moves_2[:index+1]
      for index, j in enumerate(possible_moves_3):
        if 0<j<64:
          if empty_white(j) and current_row(i) == current_row(j) and empty_black(j):
            pass
          else:
            if not empty_black(j):
              possible_moves_3 = possible_moves_3[:index]
              break
            if not empty_white(j):
              possible_moves_3 = possible_moves_3[:index+1]
      for index, j in enumerate(possible_moves_4):
        if 0<j<64:
          if empty_white(j) and current_row(i) == current_row(j) and empty_black(j):
            pass
          else:
            if not empty_black(j):
              possible_moves_4 = possible_moves_4[:index]
              break
            if not empty_white(j):
              possible_moves_4 = possible_moves_4[:index+1]

      legalMoves.extend(['q'+str(i+1)+'q' + str(move+1) for move in possible_moves_1 if 0<move<64])
      legalMoves.extend(['q'+str(i+1)+'q' + str(move+1) for move in possible_moves_2 if 0<move<64])
      legalMoves.extend(['q'+str(i+1)+'q' + str(move+1) for move in possible_moves_3 if 0<move<64])
      legalMoves.extend(['q'+str(i+1)+'q' + str(move+1) for move in possible_moves_4 if 0<move<64])
  for i in range(len(KINGS)):
    if turntype == 'w' and KINGS[i] > 0:
      possible_moves = [i-9, i-8, i-7, i-1, i+1, i+7, i+8]
      for index, j in enumerate(possible_moves):
        if 0<j<64 and empty_white(j) and abs(current_row(j)-current_row(i))<=2 and abs(current_column(j)-current_column(i))<=2:
          legalMoves.extend(['K' + str(i+1)+'K'+str(j+1)])
    if turntype == 'b' and KINGS[i] < 0:
      possible_moves = [i-9, i-8, i-7, i-1, i+1, i+7, i+8]
      for index, j in enumerate(possible_moves):
        if 0<j<64 and empty_black(j) and abs(current_row(j)-current_row(i))<=2 and abs(current_column(j)-current_column(i))<=2:
          legalMoves.extend(['k' + str(i+1)+'k' + str(j+1)])
  templists = []
  for i in range(len(legalMoves)):
    if isLegal(inputFEN, legalMoves[i], turntype) == False:
      templists.append(legalMoves[i])
  for i in templists:
    legalMoves.remove(i)
  return legalMoves
def findAttacked(inputFEN, turntype):
  global AttackedMoves
  AttackedMoves = []
  modified_string = ''.join([char for char in inputFEN])
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
            KINGS[index] = -10
            UNIONK[index] = -10
        elif item == 'K':
            KINGS[index] = 0
            UNIONK[index] = 0
        elif item == 'q':
            QUEENS[index] = -9
            UNIONNOK[index] = -9
            UNIONK[index] = -9
        elif item == 'Q':
            QUEENS[index] = 9
            UNIONNOK[index] = 9
            UNIONK[index] = 9
  for i in range(0, len(PAWNS)-1, 1): 
    if turntype == 'w':
      if PAWNS[i] > 0:
        if i-7 > 0 and i%8 != 0:
          AttackedMoves.append('p'+str(i-6))
        if i-9 > 0 and i % 8 != 1:
          AttackedMoves.append('p'+str(i-8))
    elif turntype == 'b':
      if PAWNS[i] < 0:
        if i+7 < 64 and i%8 != 1: 
          AttackedMoves.append('P'+str(i+8))
        if i+9 < 64 and i %8 != 0: 
          AttackedMoves.append('P'+str(i+10))
  for i in range(len(KNIGHTS)):
    file_i = i % 8  
    if turntype == 'w':
      if KNIGHTS[i] > 0:
        possible_moves = [
          i - 17, i - 15, i - 10, i - 6, i + 6, i + 10, i + 15, i + 17
        ]
        AttackedMoves.extend(['n' + str(move+1) for move in possible_moves if 0 < move < 64 and empty_white(move) and abs(move % 8 - file_i) <= 2])

    elif turntype == 'b':
      if KNIGHTS[i] < 0:
        possible_moves = [
          i - 17, i - 15, i - 10, i - 6, i + 6, i + 10, i + 15, i + 17
         ]
        AttackedMoves.extend(['N' + str(move+1) for move in possible_moves if 0 < move < 64 and empty_black(move) and abs(move % 8 - file_i) <= 2])
  for i in range(len(BISHOPS)):
    if turntype == 'w' and BISHOPS[i] > 0:
      possible_moves_1 = [i+7, i+14, i+21, i+28, i+35, i+42, i+49, i+56, i+63]
      possible_moves_2 = [i-7, i-14, i-21, i-28, i-35, i-42, i-49, i-56, i-63]
      possible_moves_3= [i+9, i+18, i+27, i+36, i+45, i+54, i+63]
      possible_moves_4 = [i-9, i-18, i-27, i-36, i-45, i-54, i-63]
      possible_moves_1 = possible_moves_1[:8-(i%8)]
      possible_moves_2 = possible_moves_2[:(i%8)]
      possible_moves_3 = possible_moves_3[:8-(i%8)]
      possible_moves_1 = possible_moves_1[:(i%8)]
      for index, j in enumerate(possible_moves_1):
        if 0<j<64:
          if empty_white(j) and empty_black(j) and j%8 != 0:
            pass
          else:
           if not empty_white(j): 
            possible_moves_1 = possible_moves_1[:index]
            break
           elif not empty_black(j) or j%8 == 0:
            possible_moves_1 = possible_moves_1[:index+1]
            break

      for index, j in enumerate(possible_moves_2):
        if 0<j<64:
          if empty_white(j) and empty_black(j) and j%8 != 0:
            pass
          else:
           if not empty_white(j): 
            possible_moves_2 = possible_moves_2[:index]
            break
           elif not empty_black(j) or j%8 == 0:
            possible_moves_2 = possible_moves_2[:index+1]
            break
      for index, j in enumerate(possible_moves_3):
        if 0<j<64:
          if empty_white(j) and empty_black(j) and j%8 != 0:
            pass
          else:
           if not empty_white(j): 
            possible_moves_3 = possible_moves_3[:index]
            break
           elif not empty_black(j) or j%8 == 0:
            possible_moves_3 = possible_moves_3[:index+1]
            break
      for index, j in enumerate(possible_moves_4):
        if 0<j<64:
          if empty_white(j) and empty_black(j) and j%8 != 0:
            pass
          else:
           if not empty_white(j): 
            possible_moves_4 = possible_moves_4[:index]
            break
           elif not empty_black(j) or j%8 == 0:
            possible_moves_4 = possible_moves_4[:index+1]
            break
      AttackedMoves.extend(['b' + str(move+1) for move in possible_moves_1 if 0<move<64])
      AttackedMoves.extend(['b' + str(move+1) for move in possible_moves_2 if 0<move<64])
      AttackedMoves.extend(['b' + str(move+1) for move in possible_moves_3 if 0<move<64])
      AttackedMoves.extend(['b' + str(move+1) for move in possible_moves_4 if 0<move<64])
    if turntype == 'b' and BISHOPS[i] < 0:
            possible_moves_1 = [i+7, i+14, i+21, i+28, i+35, i+42, i+49, i+56, i+63]
            possible_moves_2 = [i-7, i-14, i-21, i-28, i-35, i-42, i-49, i-56, i-63]
            possible_moves_3= [i+9, i+18, i+27, i+36, i+45, i+54, i+63]
            possible_moves_4 = [i-9, i-18, i-27, i-36, i-45, i-54, i-63]
            possible_moves_1 = possible_moves_1[:8-(i%8)]
            possible_moves_2 = possible_moves_2[:(i%8)]
            possible_moves_3 = possible_moves_3[:8-(i%8)]
            possible_moves_1 = possible_moves_1[:(i%8)]
            for index, j in enumerate(possible_moves_1):
              if 0<j<64:
                if empty_white(j) and empty_black(j) and j%8 !=0:
                  pass
                else:
                 if not empty_black(j): 
                  possible_moves_1 = possible_moves_1[:index]
                  break
                 elif not empty_white(j) or j%8 == 0:
                  possible_moves_1 = possible_moves_1[:index+1]
                  break
            for index, j in enumerate(possible_moves_2):
              if 0<j<64:
                if empty_white(j) and empty_black(j) and j%8 !=0:
                  pass
                else:
                 if not empty_black(j): 
                  possible_moves_2 = possible_moves_2[:index]
                  break
                 elif not empty_white(j) or j%8 ==0:
                  possible_moves_2 = possible_moves_2[:index+1]
                  break
            for index, j in enumerate(possible_moves_3):
              if 0<j<64:
                if empty_white(j) and empty_black(j) and j%8 !=0:
                  pass
                else:
                 if not empty_black(j): 
                  possible_moves_3 = possible_moves_3[:index]
                  break
                 elif not empty_white(j) or j%8 == 0:
                  possible_moves_3 = possible_moves_3[:index+1]
                  break
            for index, j in enumerate(possible_moves_4):
              if 0<j<64:
                if empty_white(j) and empty_black(j) and j%8 !=0:
                  pass
                else:
                 if not empty_black(j): 
                  possible_moves_4 = possible_moves_4[:index]
                  break
                 elif not empty_white(j) or j%8 == 0:
                  possible_moves_4 = possible_moves_4[:index+1]
                  break
            AttackedMoves.extend(['B' + str(move+1) for move in possible_moves_1 if 0<move<64])
            AttackedMoves.extend(['B' + str(move+1) for move in possible_moves_2 if 0<move<64])
            AttackedMoves.extend(['B' + str(move+1) for move in possible_moves_3 if 0<move<64])
            AttackedMoves.extend(['B' + str(move+1) for move in possible_moves_4 if 0<move<64])
  for i in range(len(ROOKS)):
    if turntype == 'w' and ROOKS[i] > 0:
      possible_moves_1 = [i+1, i+2, i+3, i+4, i+5, i+6, i+7]
      possible_moves_2 = [i-1, i-2, i-3, i-4, i-5, i-6, i-7]
      possible_moves_3 = [i+8, i+16, i+24, i+32, i+40, i+48, i+56]
      possible_moves_4 = [i-8, i-16, i-24, i-32, i-40, i-48, i-56]
      for index, j in enumerate(possible_moves_1):
        if 0<j<64:
          if empty_white(j) and current_row(i) == current_row(j) and empty_black(j):
            pass
          else:
            if not empty_white(j):
              possible_moves_1 = possible_moves_1[:index]
              break
            if not empty_black(j):
              possible_moves_1 = possible_moves_1[:index+1]
      for index, j in enumerate(possible_moves_2):
        if 0<j<64:
          if empty_white(j) and current_row(i) == current_row(j) and empty_black(j):
            pass
          else:
            if not empty_white(j):
              possible_moves_2 = possible_moves_2[:index]
              break
            if not empty_black(j):
              possible_moves_2 = possible_moves_2[:index+1]
      for index, j in enumerate(possible_moves_3):
        if 0<j<64:
          if empty_white(j) and current_row(i) == current_row(j) and empty_black(j):
            pass
          else:
            if not empty_white(j):
              possible_moves_3 = possible_moves_3[:index]
              break
            if not empty_black(j):
              possible_moves_3 = possible_moves_3[:index+1]
      for index, j in enumerate(possible_moves_4):
        if 0<j<64:
          if empty_white(j) and current_row(i) == current_row(j) and empty_black(j):
            pass
          else:
            if not empty_white(j):
              possible_moves_4 = possible_moves_4[:index]
              break
            if not empty_black(j):
              possible_moves_4 = possible_moves_4[:index+1]

      AttackedMoves.extend(['r' + str(move+1) for move in possible_moves_1 if 0<move<64])
      AttackedMoves.extend(['r' + str(move+1) for move in possible_moves_2 if 0<move<64])
      AttackedMoves.extend(['r' + str(move+1) for move in possible_moves_3 if 0<move<64])
      AttackedMoves.extend(['r' + str(move+1) for move in possible_moves_4 if 0<move<64])
    if turntype == 'b' and ROOKS[i] < 0:
        possible_moves_1 = [i+1, i+2, i+3, i+4, i+5, i+6, i+7]
        possible_moves_2 = [i-1, i-2, i-3, i-4, i-5, i-6, i-7]
        possible_moves_3 = [i+8, i+16, i+24, i+32, i+40, i+48, i+56]
        possible_moves_4 = [i-8, i-16, i-24, i-32, i-40, i-48, i-56]
        for index, j in enumerate(possible_moves_1):
          if 0<j<64:
            if empty_white(j) and current_row(i) == current_row(j) and empty_black(j):
              pass
            else:
              if not empty_black(j):
                possible_moves_1 = possible_moves_1[:index]
                break
              if not empty_white(j):
                possible_moves_1 = possible_moves_1[:index+1]
        for index, j in enumerate(possible_moves_2):
          if 0<j<64:
            if empty_white(j) and current_row(i) == current_row(j) and empty_black(j):
              pass
            else:
              if not empty_black(j):
                possible_moves_2 = possible_moves_2[:index]
                break
              if not empty_white(j):
                possible_moves_2 = possible_moves_2[:index+1]
        for index, j in enumerate(possible_moves_3):
          if 0<j<64:
            if empty_white(j) and current_row(i) == current_row(j) and empty_black(j):
              pass
            else:
              if not empty_black(j):
                possible_moves_3 = possible_moves_3[:index]
                break
              if not empty_white(j):
                possible_moves_3 = possible_moves_3[:index+1]
        for index, j in enumerate(possible_moves_4):
          if 0<j<64:
            if empty_white(j) and current_row(i) == current_row(j) and empty_black(j):
              pass
            else:
              if not empty_black(j):
                possible_moves_4 = possible_moves_4[:index]
                break
              if not empty_white(j):
                possible_moves_4 = possible_moves_4[:index+1]

        AttackedMoves.extend(['R' + str(move+1) for move in possible_moves_1 if 0<move<64])
        AttackedMoves.extend(['R' + str(move+1) for move in possible_moves_2 if 0<move<64])
        AttackedMoves.extend(['R' + str(move+1) for move in possible_moves_3 if 0<move<64])
        AttackedMoves.extend(['R' + str(move+1) for move in possible_moves_4 if 0<move<64])
  for i in range(len(QUEENS)):
    if turntype == 'w' and QUEENS[i] > 0:
      possible_moves_1 = [i+7, i+14, i+21, i+28, i+35, i+42, i+49, i+56, i+63]
      possible_moves_2 = [i-7, i-14, i-21, i-28, i-35, i-42, i-49, i-56, i-63]
      possible_moves_3= [i+9, i+18, i+27, i+36, i+45, i+54, i+63]
      possible_moves_4 = [i-9, i-18, i-27, i-36, i-45, i-54, i-63]
      possible_moves_1 = possible_moves_1[:8-(i%8)]
      possible_moves_2 = possible_moves_2[:(i%8)]
      possible_moves_3 = possible_moves_3[:8-(i%8)]
      possible_moves_1 = possible_moves_1[:(i%8)]
      for index, j in enumerate(possible_moves_1):
        if 0<j<64:
          if empty_white(j) and empty_black(j) and j%8 != 0:
            pass
          else:
           if not empty_white(j): 
            possible_moves_1 = possible_moves_1[:index]
            break
           elif not empty_black(j) or j%8 == 0:
            possible_moves_1 = possible_moves_1[:index+1]
            break

      for index, j in enumerate(possible_moves_2):
        if 0<j<64:
          if empty_white(j) and empty_black(j) and j%8 != 0:
            pass
          else:
           if not empty_white(j): 
            possible_moves_2 = possible_moves_2[:index]
            break
           elif not empty_black(j) or j%8 == 0:
            possible_moves_2 = possible_moves_2[:index+1]
            break
      for index, j in enumerate(possible_moves_3):
        if 0<j<64:
          if empty_white(j) and empty_black(j) and j%8 != 0:
            pass
          else:
           if not empty_white(j): 
            possible_moves_3 = possible_moves_3[:index]
            break
           elif not empty_black(j) or j%8 == 0:
            possible_moves_3 = possible_moves_3[:index+1]
            break
      for index, j in enumerate(possible_moves_4):
        if 0<j<64:
          if empty_white(j) and empty_black(j) and j%8 != 0:
            pass
          else:
           if not empty_white(j): 
            possible_moves_4 = possible_moves_4[:index]
            break
           elif not empty_black(j) or j%8 == 0:
            possible_moves_4 = possible_moves_4[:index+1]
            break
      AttackedMoves.extend(['q' + str(move+1) for move in possible_moves_1 if 0<move<64])
      AttackedMoves.extend(['q' + str(move+1) for move in possible_moves_2 if 0<move<64])
      AttackedMoves.extend(['q' + str(move+1) for move in possible_moves_3 if 0<move<64])
      AttackedMoves.extend(['q' + str(move+1) for move in possible_moves_4 if 0<move<64])
      possible_moves_1 = [i+1, i+2, i+3, i+4, i+5, i+6, i+7]
      possible_moves_2 = [i-1, i-2, i-3, i-4, i-5, i-6, i-7]
      possible_moves_3 = [i+8, i+16, i+24, i+32, i+40, i+48, i+56]
      possible_moves_4 = [i-8, i-16, i-24, i-32, i-40, i-48, i-56]
      for index, j in enumerate(possible_moves_1):
        if 0<j<64:
          if empty_white(j) and current_row(i) == current_row(j) and empty_black(j):
            pass
          else:
            if not empty_white(j):
              possible_moves_1 = possible_moves_1[:index]
              break
            if not empty_black(j):
              possible_moves_1 = possible_moves_1[:index+1]
      for index, j in enumerate(possible_moves_2):
        if 0<j<64:
          if empty_white(j) and current_row(i) == current_row(j) and empty_black(j):
            pass
          else:
            if not empty_white(j):
              possible_moves_2 = possible_moves_2[:index]
              break
            if not empty_black(j):
              possible_moves_2 = possible_moves_2[:index+1]
      for index, j in enumerate(possible_moves_3):
        if 0<j<64:
          if empty_white(j) and current_row(i) == current_row(j) and empty_black(j):
            pass
          else:
            if not empty_white(j):
              possible_moves_3 = possible_moves_3[:index]
              break
            if not empty_black(j):
              possible_moves_3 = possible_moves_3[:index+1]
      for index, j in enumerate(possible_moves_4):
        if 0<j<64:
          if empty_white(j) and current_row(i) == current_row(j) and empty_black(j):
            pass
          else:
            if not empty_white(j):
              possible_moves_4 = possible_moves_4[:index]
              break
            if not empty_black(j):
              possible_moves_4 = possible_moves_4[:index+1]

      AttackedMoves.extend(['q' + str(move+1) for move in possible_moves_1 if 0<move<64])
      AttackedMoves.extend(['q' + str(move+1) for move in possible_moves_2 if 0<move<64])
      AttackedMoves.extend(['q' + str(move+1) for move in possible_moves_3 if 0<move<64])
      AttackedMoves.extend(['q' + str(move+1) for move in possible_moves_4 if 0<move<64])
    if turntype == 'b' and QUEENS[i] < 0:
      possible_moves_1 = [i+7, i+14, i+21, i+28, i+35, i+42, i+49, i+56, i+63]
      possible_moves_2 = [i-7, i-14, i-21, i-28, i-35, i-42, i-49, i-56, i-63]
      possible_moves_3= [i+9, i+18, i+27, i+36, i+45, i+54, i+63]
      possible_moves_4 = [i-9, i-18, i-27, i-36, i-45, i-54, i-63]
      possible_moves_1 = possible_moves_1[:8-(i%8)]
      possible_moves_2 = possible_moves_2[:(i%8)]
      possible_moves_3 = possible_moves_3[:8-(i%8)]
      possible_moves_1 = possible_moves_1[:(i%8)]
      for index, j in enumerate(possible_moves_1):
        if 0<j<64:
          if empty_white(j) and empty_black(j) and j%8 !=0:
            pass
          else:
           if not empty_black(j): 
            possible_moves_1 = possible_moves_1[:index]
            break
           elif not empty_white(j) or j%8 == 0:
            possible_moves_1 = possible_moves_1[:index+1]
            break
      for index, j in enumerate(possible_moves_2):
        if 0<j<64:
          if empty_white(j) and empty_black(j) and j%8 !=0:
            pass
          else:
           if not empty_black(j): 
            possible_moves_2 = possible_moves_2[:index]
            break
           elif not empty_white(j) or j%8 ==0:
            possible_moves_2 = possible_moves_2[:index+1]
            break
      for index, j in enumerate(possible_moves_3):
        if 0<j<64:
          if empty_white(j) and empty_black(j) and j%8 !=0:
            pass
          else:
           if not empty_black(j): 
            possible_moves_3 = possible_moves_3[:index]
            break
           elif not empty_white(j) or j%8 == 0:
            possible_moves_3 = possible_moves_3[:index+1]
            break
      for index, j in enumerate(possible_moves_4):
        if 0<j<64:
          if empty_white(j) and empty_black(j) and j%8 !=0:
            pass
          else:
           if not empty_black(j): 
            possible_moves_4 = possible_moves_4[:index]
            break
           elif not empty_white(j) or j%8 == 0:
            possible_moves_4 = possible_moves_4[:index+1]
            break
      AttackedMoves.extend(['Q' + str(move+1) for move in possible_moves_1 if 0<move<64])
      AttackedMoves.extend(['Q' + str(move+1) for move in possible_moves_2 if 0<move<64])
      AttackedMoves.extend(['Q' + str(move+1) for move in possible_moves_3 if 0<move<64])
      AttackedMoves.extend(['Q' + str(move+1) for move in possible_moves_4 if 0<move<64])
      possible_moves_1 = [i+1, i+2, i+3, i+4, i+5, i+6, i+7]
      possible_moves_2 = [i-1, i-2, i-3, i-4, i-5, i-6, i-7]
      possible_moves_3 = [i+8, i+16, i+24, i+32, i+40, i+48, i+56]
      possible_moves_4 = [i-8, i-16, i-24, i-32, i-40, i-48, i-56]
      for index, j in enumerate(possible_moves_1):
        if 0<j<64:
          if empty_white(j) and current_row(i) == current_row(j) and empty_black(j):
            pass
          else:
            if not empty_black(j):
              possible_moves_1 = possible_moves_1[:index]
              break
            if not empty_white(j):
              possible_moves_1 = possible_moves_1[:index+1]
      for index, j in enumerate(possible_moves_2):
        if 0<j<64:
          if empty_white(j) and current_row(i) == current_row(j) and empty_black(j):
            pass
          else:
            if not empty_black(j):
              possible_moves_2 = possible_moves_2[:index]
              break
            if not empty_white(j):
              possible_moves_2 = possible_moves_2[:index+1]
      for index, j in enumerate(possible_moves_3):
        if 0<j<64:
          if empty_white(j) and current_row(i) == current_row(j) and empty_black(j):
            pass
          else:
            if not empty_black(j):
              possible_moves_3 = possible_moves_3[:index]
              break
            if not empty_white(j):
              possible_moves_3 = possible_moves_3[:index+1]
      for index, j in enumerate(possible_moves_4):
        if 0<j<64:
          if empty_white(j) and current_row(i) == current_row(j) and empty_black(j):
            pass
          else:
            if not empty_black(j):
              possible_moves_4 = possible_moves_4[:index]
              break
            if not empty_white(j):
              possible_moves_4 = possible_moves_4[:index+1]

      AttackedMoves.extend(['Q' + str(move+1) for move in possible_moves_1 if 0<move<64])
      AttackedMoves.extend(['Q' + str(move+1) for move in possible_moves_2 if 0<move<64])
      AttackedMoves.extend(['Q' + str(move+1) for move in possible_moves_3 if 0<move<64])
      AttackedMoves.extend(['Q' + str(move+1) for move in possible_moves_4 if 0<move<64])
  for i in range(len(KINGS)):
    if turntype == 'w' and KINGS[i] > 0:
      possible_moves = [i-9, i-8, i-7, i-1, i+1, i+7, i+8]
      for index, j in enumerate(possible_moves):
        if 0<j<64 and empty_white(j):
          AttackedMoves.extend(['k' + str(j+1)])
    if turntype == 'b' and KINGS[i] < 0:
      possible_moves = [i-9, i-8, i-7, i-1, i+1, i+7, i+8]
      for index, j in enumerate(possible_moves):
        if 0<j<64 and empty_black(j):
          AttackedMoves.extend(['K' + str(j+1)])
  tempolist=[]
  ATTACKEDSQUARES = []
  for i in range(len(AttackedMoves)):
    tempvari = AttackedMoves[1:]
    ATTACKEDSQUARES.append([tempvari])
  for i in range(len(AttackedMoves)):
    tempvari = ''.join(char for char in AttackedMoves[i] if not char.isalpha())
    tempolist.append(int(tempvari))
  AttackedMoves =[]
  for item in tempolist:
    AttackedMoves.append(item)
  return AttackedMoves
def evaluate(iiiFEN):
  basillist = returnconvert(iiiFEN)
  eval =0
  for i in basillist:
    eval+=i
  for i, value in enumerate(basillist):
    if value != 0:
      if int(value) == 1:
        eval += listp[i]
      if int(value) == 4:
        eval += listb[i]
      if int(value) == 3:
        eval += listn[i]
      if int(value) == 5:
        eval += listr[i]
      if int(value) == 9:
        eval += listq[i]
      if int(value) == 10:
        eval += listk[i]
      if int(value) == -1:
        eval -= listp[63-i]
      if int(value) == -4:
        eval -= listb[63-i]
      if int(value) == -3:
        eval -= listn[63-i]
      if int(value) == -5:
        eval -= listr[63-i]
      if int(value) == -9:
        eval -= listq[63-i]
      if int(value) == -10:
        eval -= listk[63-i]
  return round(eval, 2) 
def evaluatechange(iiiFEN, turnn, move):
  if turnn == 'w':
    c = 'b'
  if turnn == 'b':
    c = 'w'
  for i in range(len(move)):
    if move[i].isalpha() and i !=1:
      futmove = move[:i]
      remmove = move[i:]
  ball= re.sub(r'(\d+)', lambda match: 'l' * int(match.group()), iiiFEN)
  moveFEN = ball.replace('/', '')
  piecename = move[:1]
  indexnum = int(remmove[1:])
  orig_index = int(futmove[1:])
  moveFEN = moveFEN[:orig_index-1] + 'l' + moveFEN[orig_index:]
  moveFEN = moveFEN[:]
  moveFEN = moveFEN[:indexnum-1] + piecename + moveFEN[indexnum:]
  moveFEN = re.sub(r'l+', lambda match: str(len(match.group())), moveFEN)
  return evaluate(moveFEN)
def isLegal(startingFEN, move, turntype):
  convert(startingFEN)
  king =0
  if turntype ==  'w':
    turni = 'b'
    for i in KINGS:
      if i>0:
        king = KINGS.index(i)
        break
  elif turntype == 'b':
    turni = 'w'
    for i in KINGS:
      if i<0:
        king = KINGS.index(i)
        break
  for i in range(len(move)):
    if move[i].isalpha() and i !=1:
      futmove = move[:i]
      remmove = move[i:]
  ball= re.sub(r'(\d+)', lambda match: 'l' * int(match.group()), startingFEN)
  moveFEN = ball.replace('/', '')
  piecename = move[:1]
  indexnum = int(remmove[1:])
  orig_index = int(futmove[1:])
  moveFEN = moveFEN[:orig_index-1] + 'l' + moveFEN[orig_index:]
  moveFEN = moveFEN[:]
  moveFEN = moveFEN[:indexnum-1] + piecename + moveFEN[indexnum:]
  moveFEN = re.sub(r'l+', lambda match: str(len(match.group())), moveFEN)
  xlist = findAttacked(moveFEN, turni)
  if not piecename == 'k' and not piecename == 'K':
    for i in xlist:
      if int(i) == king+1:
        return False
    return True
  else: 
    king = indexnum
    for i in xlist:
      if int(i) == king:
        return False
    return True
def bestmovenobrain(startingFEN, turntype):
  firstlayereval = []
  if turntype == 'w':
    alpha = evaluate(startingFEN)
  elif turntype == 'b':
    beta = evaluate(startingFEN)
  legality = findLegal(startingFEN, turntype)
  for i in legality:
    bbb =evaluatechange(startingFEN, turntype, i)
    firstlayereval.append(bbb)
  if turntype == 'w':
    return legality[firstlayereval.index(max(firstlayereval))]
  elif turntype == 'b':
    return legality[firstlayereval.index(min(firstlayereval))]
def layer(startingFEN, turntype):
  firstlayereval = []
  if turntype == 'w':
    alpha = evaluate(startingFEN)
  elif turntype == 'b':
    beta = evaluate(startingFEN)
  legality = findLegal(startingFEN, turntype)
  for i in legality:
    bbb =evaluatechange(startingFEN, turntype, i)
    firstlayereval.append(bbb)
  return firstlayereval
def changethefen(iiiFEN, move):
  for i in range(len(move)):
    if move[i].isalpha() and i !=1:
      futmove = move[:i]
      remmove = move[i:]
  ball= re.sub(r'(\d+)', lambda match: 'l' * int(match.group()), iiiFEN)
  moveFEN = ball.replace('/', '')
  piecename = move[:1]
  indexnum = int(remmove[1:])
  orig_index = int(futmove[1:])
  moveFEN = moveFEN[:orig_index-1] + 'l' + moveFEN[orig_index:]
  moveFEN = moveFEN[:]
  moveFEN = moveFEN[:indexnum-1] + piecename + moveFEN[indexnum:]
  moveFEN = re.sub(r'l+', lambda match: str(len(match.group())), moveFEN)
  return moveFEN
def minimax(startingFEN, turntype, depth):
  EVALTREE =[]
  FENTREE= []
  NUMBERS = []
  for i in range(0, depth):
    if i == 0:
      EVALTREE.append(layer(startingFEN, turntype))
def LAGnormal(move, startingFEN, turntype): 
  for i in range(len(move)):
    if move[i].isalpha() and i !=1:
      futmove = move[i:]
  output = futmove[0]+'x'
  num=  int(futmove[1:])
  if num%8 == 1:
    output += 'a'
  if num%8 == 2:
    output += 'b'
  if num%8 == 3:
    output += 'c'
  if num%8 == 4:
    output += 'd'
  if num%8 == 5:
    output += 'e'
  if num%8 == 6:
    output += 'f'
  if num%8 == 7:
    output += 'g'
  if num%8 == 0:
    output += 'h'
  output += str(8-num//8)
  return output