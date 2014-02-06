from copy import deepcopy
DIRECTIONS = [(1,-1),(1,0),(1,1),(0,1),(-1,-1),(-1,0),(-1,1),(0,-1)]
BLACK, WHITE = 1,-1
class Board:
	def __init__(self, b):
		#utility is nbr of black tiles minus nbr of white tiles. AI is black.
		self.utility = 0
		#Deep copy, for silly reasons
		self.board = deepcopy(b)

	def within_board(self, i):
		return 0 <= i < 8

	def alph_to_num(self, letter):
		return ord(letter) - 97

	def num_to_alph(self, num):
		return chr(num + 97)

	def print_board(self):
		print "  a b c d e f g h"
		i = 1
		for row in self.board:
			print i,
			i +=1
			for col in row:
				if col == BLACK:
					print "B",
				elif col == WHITE:
					print "W",
				else:
					print col,
			print "\n"
		print "\n"

	def find_legal_moves(self, player):
		"""For every brick that current player owns, search in all directions.
			A legal placement is if there is an empty space following consecutive opponent bricks"""
		legal_moves = []
		for row in range(8):
			for col in range(8):
				if self.board[row][col] == player:
					for tup in DIRECTIONS:
						new_row = row + tup[0]
						new_col = col + tup[1]
						legal = 0
						bracket = 0
						while self.within_board(new_row) and self.within_board(new_col):
							if self.board[new_row][new_col] == player:
								legal = 0
								break
							elif self.board[new_row][new_col] == -player:
								legal = 1
								new_row += tup[0]
								new_col += tup[1]
							elif self.board[new_row][new_col] == 0 and legal == 1:
								bracket = 1
								break
							else:
								break
						if bracket == 1 and (new_row,new_col) not in legal_moves:
							legal_moves.append((new_row,new_col))
		return legal_moves


	def place_brick(self,player,row,col):
		# print "placed", player, "brick at pos",x,y
		if (row,col) not in self.find_legal_moves(player):
			return 0
		self.board[row][col] = player
		self.flip_bricks(player,row,col)
		self.calc_utility()
		return 1

	def calc_utility(self):
		w, b = 0,0
		for row in range(8):
			for col in range(8):
				if self.board[row][col] == WHITE:
					w += 1
				if self.board[row][col] == BLACK:
					b += 1
		self.utility = b - w

	def flip_bricks(self,player,row,col):
		for tup in DIRECTIONS:
			new_row = row + tup[0]
			new_col = col + tup[1]
			bracket = 0
			flip = 0
			while self.within_board(new_row) and self.within_board(new_col):
				if self.board[new_row][new_col] == -player:
					bracket = 1
					new_row+=tup[0]
					new_col+=tup[1]
				elif self.board[new_row][new_col] == player:
					if bracket == 1:
						flip = 1
						break
					else:
						break
				elif self.board[new_row][new_col] == 0:
					break
			if flip == 1:
				new_row = row + tup[0]
				new_col = col + tup[1]
				while self.board[new_row][new_col] != player:
					self.board[new_row][new_col] = player
					new_row+=tup[0]
					new_col+=tup[1]
		
