FENnotation = input('Enter code in FEN or Forsyth Edward Notation(please only include first 8 strings): ')
turn = input("Who's turn is it? Type w if White and type b if Black?: ")
print(FENnotation)
print(turn)
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
def conversion():
	for char in FENnotation:
		FENCHANGE.append(char)
	
	for index, item in enumerate(FENCHANGE):
		while tempvar > 0:
			if tempvar > 0:
				tempvar = tempvar-1
			if item == 'r' and tempvar <= 0:
					ROOKS[index] = 5
					UNIONNOK[index] = 5
					UNIONK[index] = 5
			elif item == 'R' and tempvar <= 0:
					ROOKS[index] = -5
					UNIONNOK[index] = -5
					UNIONK[index] = -5
			elif item == 'n' and tempvar <= 0:
					KNIGHTS[index] = 3
					UNIONNOK[index] = 3
					UNIONK[index] = 3
			elif item == 'N' and tempvar <= 0:
					KNIGHTS[index] = -3
					UNIONNOK[index] = -3
					UNIONK[index] = -3
			elif item == 'b' and tempvar <= 0:
					BISHOPS[index] = 4
					UNIONNOK[index] = 4
					UNIONK[index] = 4
			elif item == 'B' and tempvar <= 0:
					BISHOPS[index] = -4
					UNIONNOK[index] = -4
					UNIONK[index] = -4
			elif item == 'p' and tempvar <= 0:
					PAWNS[index] = 1
					UNIONNOK[index] = 1
					UNIONK[index] = 1
			elif item == 'P' and tempvar <= 0:
					PAWNS[index] = -1
					UNIONNOK[index] = -1
					UNIONK[index] = -1
			elif item == 'k' and tempvar <= 0:
					KINGS[index] = 127
					UNIONK[index] = 127
			elif item == 'K' and tempvar <= 0:
					KINGS[index] = -127 
					UNIONK[index] = -127
			elif item == 'q' and tempvar <= 0:
					QUEENS[index] = 9
					UNIONNOK[index] = 9
					UNIONK[index] = 9
			elif item == 'Q' and tempvar <= 0:
					QUEENS[index] = -9
					UNIONNOK[index] = -9
					UNIONK[index] = -9
			elif isnumeric(item) == True:
					for v in range(int(item)+1):
							PAWNS[index+v-1] = 0
							QUEENS[index+v-1] = 0
							KINGS[index+v-1] = 0
							BISHOPS[index+v-1] = 0
							ROOKS[index+v-1] = 0
							UNIONK[index+v-1] = 0
							UNIONNOK[index+v-1] = 0
							tempvar = item

def findLegal():
	for i in PAWNS :
		if  PAWNS[i] == 1 :
			if turn == 'w' :
				if i+8 < 64 :
					legalMoves.append(('Pawn',(i-8)//8,(i-8) % 8))
				if (i>7 and i<16) or (i>47 and i<56): 
						legalMoves.append(('Pawn',(i-16)//8,(i-16) % 8))
				for j in UNIONNOK:
						if UNIONNOK[j-9] > 0:
							legalMoves.append(('Pawn',(j-9)//8,(j-9) % 8))
						if UNIONNOK[j-7] > 0:
							legalMoves.append(('Pawn',(j-7)//8,(j-7) % 8))
				for z in KINGS:
						if KINGS[z-9] > 0:
							if turn == 'w' and KINGS[z-9] == 127 :
								legalMoves.append('ILLEGAL POSITION')
							if turn == 'b' and KINGS[z-9] == -127 :
								legalMoves.append('ILLEGAL POSITION')
							if turn == 'w' and KINGS[z-9] == -127 :
								legalMoves.append('CHECK')
							if turn == 'b' and KINGS[z-9] == 127 :
								legalMoves.append('CHECK')
				for z in KINGS:
						if KINGS[z-7] > 0 and turn == 'w':
							if KINGS[z-7] == 127:
										legalMoves.append('ILLEGAL POSITION')
							if turn == 'b' and KINGS[z-7] == -127 :
									legalMoves.append('ILLEGAL POSITION')
							if turn == 'w' and KINGS[z-7] == -127 :
										legalMoves.append('CHECK')
							if turn == 'b' and KINGS[z-7] == 127 :
										legalMoves.append('CHECK')      
			elif turn ==  'b' :
				if i+8 < 64 :
					legalMoves.append(('Pawn',(i-8)//8,(i-8) % 8))
				if (i>7 and i<16) or (i>47 and i<56): 
						legalMoves.append(('Pawn',(i-16)//8,(i-16) % 8))
				for j in UNIONNOK:
						if UNIONNOK[j-9] < 0:
							legalMoves.append(('Pawn',(j-9)//8,(j-9) % 8))
						if UNIONNOK[j-7] < 0:
							legalMoves.append(('Pawn',(j-7)//8,(j-7) % 8))
				for z in KINGS:
						if KINGS[z-9] < 0:
							if turn == 'w' and KINGS[z-9] == 127 :
								legalMoves.append('ILLEGAL POSITION')
							if turn == 'b' and KINGS[z-9] == -127 :
								legalMoves.append('ILLEGAL POSITION')
							if turn == 'w' and KINGS[z-9] == -127 :
								legalMoves.append('CHECK')
							if turn == 'b' and KINGS[z-9] == 127 :
								legalMoves.append('CHECK')
				for z in KINGS:
						if KINGS[z-7] < 0 and turn == 'w':
							if KINGS[z-7] == 127:
										legalMoves.append('ILLEGAL POSITION')
							if turn == 'b' and KINGS[z-7] == -127 :
									legalMoves.append('ILLEGAL POSITION')
							if turn == 'w' and KINGS[z-7] == -127 :
										legalMoves.append('CHECK')
							if turn == 'b' and KINGS[z-7] == 127 :
										legalMoves.append('CHECK')
def evaluate():
		# Finding all legal moves

		pass
conversion() 
findLegal() 
for x in range(len(UNIONNOK)):
	print(UNIONNOK[x])