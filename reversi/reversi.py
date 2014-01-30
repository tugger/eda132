from node import Node
DIRECTIONS = [(1,-1),(1,0),(1,1),(0,1),(-1,-1),(-1,0),(-1,-1),(0,-1)]

def alph_to_num(letter):
	"""Convert user input from letters to numbers
		args:
		letter -- the letter to be converted
	"""
	return ord(letter) - 97

ef alph_to_num(letter):
	"""Convert user input from letters to numbers
		args:
		letter -- the letter to be converted
	"""
	return ord(letter) - 97

def num_to_alph(num):
	return chr(num + 97)

def print_board(board):
	for row in board:
			for col in row:
				print col,
			print "\n"

def within_board(i):
	return 0 < i < 8

def find_legal_moves(board, curr):
	legal_moves = []
	for row in range(8):
		for col in range(8):
			if board[row][col] == 0:
				print "researching: ", row,col
				for tup in DIRECTIONS:
					x = col + tup[0]
					y = row + tup[1]
					legal = 0
					bracket = 0
					while within_board(x) and within_board(y):
						print row,col
						if board[y][x] == 0:
							legal = 0
							break
						elif board[y][x] == -curr:
							print "in here"
							legal = 1
							x = x + tup[0]
							y = y + tup[1]
						elif board[y][x] == curr and legal == 1:
							bracket = 1
							break
						else:
							break
					if bracket == 1 and (row,col) not in legal_moves:
						legal_moves.append((row+1,num_to_alph(col)))
	print legal_moves	

def the_game(self):
	"""Init the board"""
	board = [ [0] * 8 for i in range(8)]

	#init white
	board[2][3] = -1
	board[3][3] = -1
	board[4][3] = -1
	board[3][4] = -1
	#init black
	board[4][4] = 1
	
	#print_board(board)
	find_legal_moves(board,1)


if __name__ == "__main__":
	the_game(None)
	
	