#IMPORTANT NOTES!!!
#1. negative numbers are blacks and positive numbers are whites lowercase white uppercase black
import re

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

def conversion(FEN):
	global modified_string
	modified_string = ''.join([char for char in FEN])
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
def findLegal(turn):
	for i in range(0, len(PAWNS)-1, 1): 
		if turn.lower() == 'w':
			if PAWNS[i] > 0:
				if empty(i-8):
					legalMoves.append('p'+str(i-7))
				if i-7 > 0 and not empty_black(i-7) and i%8 != 0:
					legalMoves.append('p'+str(i-6))
				if i-9 > 0 and not empty_black(i-9) and i % 8 != 1:
					legalMoves.append('p'+str(i-8))
				if i//8 == 6 and empty(i-8) and empty(i-16):
					legalMoves.append('p'+str(i-15))
		elif turn.lower() == 'b':
			if PAWNS[i] < 0:
				if empty(i-8):
					legalMoves.append('P'+str(i+9))
				if i+7 < 64 and not empty_white(i+7) and i%8 != 1: 
					legalMoves.append('P'+str(i+8))
				if i+9 < 64 and not empty_white(i+9) and i %8 != 0: 
					legalMoves.append('P'+str(i+10))
				if i//8 == 1 and empty(i+8) and empty(i+16):
					legalMoves.append('p'+str(i+17))
	for i in range(len(KNIGHTS)):
		file_i = i % 8  
		if turn.lower() == 'w':
			if KNIGHTS[i] > 0:
				possible_moves = [
					i - 17, i - 15, i - 10, i - 6, i + 6, i + 10, i + 15, i + 17
				]
				legalMoves.extend(['n' + str(move+1) for move in possible_moves if 0 < move < 64 and empty_white(move) and abs(move % 8 - file_i) <= 2])

		elif turn.lower() == 'b':
			if KNIGHTS[i] < 0:
				possible_moves = [
					i - 17, i - 15, i - 10, i - 6, i + 6, i + 10, i + 15, i + 17
				 ]
				legalMoves.extend(['N' + str(move+1) for move in possible_moves if 0 < move < 64 and empty_black(move) and abs(move % 8 - file_i) <= 2])
	for i in range(len(BISHOPS)):
		if turn.lower() == 'w':
			possible_moves = [ i-9, i-18, i-27, i-36, i-45, i-54, i-63, i+9, i+18, i+27, i+36, i+45, i+54, i+63]
			for j in range(1,len(possible_moves)):
				if empty_white(j):
					legalMoves.append('b')
	return legalMoves

def evaluate():
		for u in range(len(UNIONNOK)):
			global eval
			eval = eval + UNIONNOK[u]
		return eval