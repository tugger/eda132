class Node:
	def __init__(self, parent, name):
		self.name = name
		self.parent = parent
		self.children = []

	
	def printName(self):
		print name