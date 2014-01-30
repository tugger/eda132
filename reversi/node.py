class Node:
	def __init__(self, parent, name):
		self.parent = parent
		self.children = []
		self.board = [ [0] * 8 for i in range(8)]

	
	def printName(self):
		print self.name