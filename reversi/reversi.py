#!/usr/bin/python
# -*- coding: utf-8 -*-
from node import Node
from board import Board
import time
import re
import sys

DIRECTIONS = [(1,-1),(1,0),(1,1),(0,1),(-1,-1),(-1,0),(-1,1),(0,-1)]
BLACK, WHITE = 1,-1

def set_up():
	board = [ [0] * 8 for i in range(8)]
	#init white
	board[3][3] = WHITE
	board[4][4] = WHITE
	#init black
	board[4][3] = BLACK
	board[3][4] = BLACK

	b = Board(board,4)
	return b

def is_numerical(i):
	try:
		float(i)
		return 1
	except ValueError:
		return 0

def correct_input(s):
	if(len(s) == 2):
		if(re.search(r"[a-h][1-8]",s)):
			return 1

def the_game(time_limit):
	current_board= set_up()
	current_board.print_board()
	break_cond = 0
	depth = 4
	while(break_cond<2):
		#if break_cond == 2 then break big while loop
		break_cond =0
		if len(current_board.find_legal_moves(WHITE)) > 0:
			brick_placed = 0
			while brick_placed == 0:
				info = raw_input('Make your move\n')
				while(not correct_input(info)):
					info = raw_input('Wrong input. Use XY where X is a-h, Y is 1-8\n')
				brick_placed = current_board.place_brick(WHITE,int(info[1])-1,ord(info[0])-97)
				if brick_placed == 0:
					print "Illegal move"
			depth += 1
			print "Your move"

			current_board.print_board()
			print ""
		else:
			break_cond += 1
		if len(current_board.find_legal_moves(BLACK)) > 0:
			root = Node(current_board,BLACK)
			root = play_turn(root,time_limit,depth)
			depth += 1
			current_board = root.board
			print "AI's move"
			current_board.print_board()
		else:
			break_cond += 1
	winner = current_board.calc_winner()
	if winner == "DRAW":
		print "It's a draw"
	else:
		print "Winner is",winner

def play_turn(root,time_limit,depth):
	endTime = int(round(time.time() * 1000)) + time_limit
	best_choice = None

	while(int(round(time.time() * 1000)) < endTime):
		tree_builder(root,endTime,depth)
		current_choice = minimax(root,endTime)
		if int(round(time.time() * 1000)) < endTime:
			best_choice = current_choice
	return best_choice



def tree_builder(node,endTime,depth):
	currTime = int(round(time.time() * 1000))
	if currTime > endTime:
		return
	if len(node.children) == 0:
		build_two_levels(node,depth)
	else:
		for child in node.children:
			tree_builder(child,endTime,depth)


def build_two_levels(node,depth):
	node.make_children(depth)
	for child in node.children:
		child.make_children(depth)


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
		i += 1
	return state.children[pos]

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
	if len(sys.argv) == 2:
		if is_numerical(sys.argv[1]):
			print "Welcome to reversi! You play as white (⬤ )"
			print sys.argv[1], "ms"
			the_game(int(sys.argv[1]))
		else:
			print "Usage: reversi.py x, where x is numerical"
			print "Or: reversi.py. Program will use default value 1000 ms"
	elif len(sys.argv) == 1:
		print "Welcome to reversi! You play as white (W)"
		print "Default value: 1000 ms"
		the_game(1000)
	else:
		print "Usage: reversi.py x, where x is numerical"
		print "Or: reversi.py. Program will use default value 1000 ms"
	
	