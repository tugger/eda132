from board import Board
class Node:
	def __init__(self,board, player):
		self.children = []
		self.board = board
		self.player = player
		#self.alpha = 0
		#self.beta = 0

	def print_state(self):
		self.board.print_board()

	def legal_moves(self, player):
		return self.board.find_legal_moves(player)

	def make_children(self):
		legal_moves = self.board.find_legal_moves(self.player)
		for move in legal_moves:
			b = Board(self.board.board)
			b.place_brick(self.player,move[0],move[1])
			n = Node(b, -self.player)
			self.children.append(n)

	def kill_children(self):
		self.children = []
		self.parent = None
