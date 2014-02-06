from node import Node
from board import Board
import time
import re
import sys
DIRECTIONS = [(1,-1),(1,0),(1,1),(0,1),(-1,-1),(-1,0),(-1,1),(0,-1)]
BLACK, WHITE = 1,-1
"""
def example(self):
	board = set_up()

	print_board(board)
	legal = find_legal_moves(board,BLACK)
	print_legal_moves(legal)
	place_brick(board,BLACK,legal[1][0],legal[1][1])
	print_board(board)
	print_legal_moves(find_legal_moves(board,WHITE))

	place_brick(board,WHITE,4,2)
	print_board(board)
"""
def set_up():
	board = [ [0] * 8 for i in range(8)]
	#init white
	board[3][3] = WHITE
	board[4][4] = WHITE
	#init black
	board[4][3] = BLACK
	board[3][4] = BLACK

	b = Board(board)
	return b

def correct_input(s):
	if(len(s) == 2):
		if(re.search(r"[a-h][1-8]",s)):
			return 1

def the_game(time_limit):
	current_board= set_up()
	current_board.print_board()
	break_cond = 0
	while(break_cond<2):
		#if break_cond == 2 then break big while loop
		break_cond =0
		if len(current_board.find_legal_moves(WHITE)) > 0:
			brick_placed = 0
			while brick_placed == 0:
				info = raw_input('Make your move, press p for current board\n')
				if info == 'p':
					current_board.print_board()
				while(not correct_input(info)):
					info = raw_input('Wrong input. Use XY where X is a-h, Y is 1-8\n')
				brick_placed = current_board.place_brick(WHITE,int(info[1])-1,ord(info[0])-97)
				if brick_placed == 0:
					print "Illegal move"
		else:
			break_cond += 1
		if len(current_board.find_legal_moves(BLACK)) > 0:
			root = Node(current_board,BLACK)
			root = play_turn(root,time_limit)
			root.kill_children()
			current_board = root.board
			print "AI made hens move"
		else:
			break_cond += 1



def play_turn(root,time_limit):
	endTime = int(round(time.time() * 1000)) + time_limit
	best_choice = None

	while(int(round(time.time() * 1000)) < endTime):
		tree_builder(root,endTime)
		best_choice = minimax(root,endTime)
	# for c in root.children:
	# 	c.print_state()
	return best_choice



def tree_builder(node,endTime):
	currTime = int(round(time.time() * 1000))
	if currTime > endTime:
		return
	if len(node.children) == 0:
		build_two_levels(node)
	else:
		for child in node.children:
			tree_builder(child,endTime)


def build_two_levels(node):
	node.make_children()
	for child in node.children:
		child.make_children()


"""THE ALGORITHM!!"""
def minimax(state, endTime):
	v = -sys.maxint -1
	i = 0
	pos = 0
	for child in state.children:
		currTime = int(round(time.time() * 1000))
		if currTime > endTime:
			break
		new_v = min_value(child,0,0,endTime)
		if new_v > v:
			pos = i
			v = new_v
		else:
			i += 1
	return state.children[pos]

	#find max for all actions

def max_value(state,a,b,endTime):
	currTime = int(round(time.time() * 1000))
	if len(state.children) == 0 or currTime > endTime:
		return state.board.utility
	else:
		v = -sys.maxint -1
		for child in state.children:
			v = max(v,min_value(child,a,b,endTime))
			if v >= b:
				return v
			a = max(v,a)
		return v

def min_value(state,a,b,endTime):
	currTime = int(round(time.time() * 1000))
	if len(state.children) == 0 or currTime > endTime:
		return state.board.utility
	else:
		v = sys.maxint
		for child in state.children:
			v = min(v, max_value(child,a,b,endTime))
			if v <= a:
				return v
			b = min(v,b)
		return v

if __name__ == "__main__":
	#example(None)
	the_game(1000)
	
	