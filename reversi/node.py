from board import Board
class Node:
	def __init__(self,board, player):
		self.children = []
		self.board = board
		self.player = player

	def print_state(self):
		self.board.print_board()

	def legal_moves(self, player):
		return self.board.find_legal_moves(player)

	def make_children(self, depth):
		legal_moves = self.board.find_legal_moves(self.player)
		for move in legal_moves:
			b = Board(self.board.board, depth)
			b.place_brick(self.player,move[0],move[1])
			n = Node(b, -self.player)
			self.children.append(n)
