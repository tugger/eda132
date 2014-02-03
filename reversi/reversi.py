from node import Node

DIRECTIONS = [(1,-1),(1,0),(1,1),(0,1),(-1,-1),(-1,0),(-1,-1),(0,-1)]
BLACK, WHITE = 1,-1

def alph_to_num(letter):
	return ord(letter) - 97

def num_to_alph(num):
	return chr(num + 97)

def print_board(board):
	for row in board:
			for col in row:
				if col == BLACK:
					print "B",
				elif col == WHITE:
					print "W",
				else:
					print col,
			print "\n"
	print "\n"

def within_board(i):
	return 0 < i < 8

def place_brick(board,curr,x,y):
	board[x][y] = curr
	flip_bricks(board,curr,x,y)

def flip_bricks(board,curr,x,y):
	for tup in DIRECTIONS:
		newx = x + tup[0]
		newy = y + tup[1]
		bracket = 0
		flip = 0
		while within_board(newx) and within_board(newy):
			if board[newx][newy] == -curr:
				bracket = 1
				newx+=tup[0]
				newy+=tup[1]
			if board[newx][newy] == curr:
				if bracket == 1:
					flip = 1
					break
				else:
					break
			if board[newx][newy] == 0:
				break
		if flip == 1:
			newx = x + tup[0]
			newy = y + tup[1]
			while board[newx][newy] != curr:
				board[newx][newy] = curr
				newx+=tup[0]
				newy+=tup[1]


def find_legal_moves(board, curr):
	"""For every brick that current player owns, search in all directions.
		A legal placement is if there is an empty space following consecutive opponent bricks"""
	legal_moves = []
	for row in range(8):
		for col in range(8):
			if board[row][col] == curr:
				for tup in DIRECTIONS:
					x = col + tup[0]
					y = row + tup[1]
					legal = 0
					bracket = 0
					while within_board(x) and within_board(y):
						if board[y][x] == curr:
							legal = 0
							break
						elif board[y][x] == -curr:
							legal = 1
							x = x + tup[0]
							y = y + tup[1]
						elif board[y][x] == 0 and legal == 1:
							bracket = 1
							break
						else:
							break
					if bracket == 1 and (x,y) not in legal_moves:
						legal_moves.append((x,y))
	return legal_moves

def the_game(self):
	"""Init the board"""
	board = [ [0] * 8 for i in range(8)]

	#init white
	board[3][3] = -1
	board[4][4] = -1
	#init black
	board[4][3] = 1
	board[3][4] = 1
	print_board(board)
	legal = find_legal_moves(board,1)
	place_brick(board,BLACK,legal[1][0],legal[1][1])
	print_board(board)
	place_brick(board,WHITE,4,2)
	print_board(board)

if __name__ == "__main__":
	the_game(None)
	
	