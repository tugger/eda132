#!/usr/bin/python
# -*- coding: utf-8 -*-
from copy import deepcopy
DIRECTIONS = [(1, -1), (1, 0), (1, 1), (0, 1), (-1, -1), (-1, 0), (-1, 1), (0, -1)]
BLACK, WHITE = 1, -1


class Board:
    def __init__(self, b, depth):
        # utility is nbr of black tiles minus nbr of white tiles. AI is black.
        self.utility = 0
        self.white_moves = None
        self.black_moves = None
        self.placed_bricks = 0
        self.starting_depth = depth
        # Deep copy, for silly reasons
        self.board = deepcopy(b)

    def within_board(self, i):
        return 0 <= i < 8

    def alph_to_num(self, letter):
        return ord(letter) - 97

    def num_to_alph(self, num):
        return chr(num + 97)

    def print_board(self):
        print "   a   b   c   d   e   f   g   h"
        print " ╔═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╗"

        for row in range(0,8):
            s = str(row+1) + "║"
            for col in range(0,8):
                if self.board[row][col] == 0:
                    s += "   "
                elif  self.board[row][col] == -1:
                    s += " ⬤ " #white
                elif self.board[row][col] == 1:
                    s += " ◯ " #black
                s += "║"
            print s
            if row < 7:
                print " ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣"
            else:
                print " ╚═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╝"

    def find_legal_moves(self, player):
        """For every brick that current player owns, search in all directions.
            A legal placement is if there is an empty space following consecutive opponent bricks"""
        if player == BLACK and self.black_moves is not None:
            return self.black_moves
        elif self.white_moves is not None:
            return self.white_moves
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
        if player == BLACK:
            self.black_moves = legal_moves
        else:
            self.white_moves = legal_moves
        return legal_moves

    def place_brick(self,player,row,col):
        # print "placed", player, "brick at pos",x,y
        if (row,col) not in self.find_legal_moves(player):
            return 0
        self.board[row][col] = player
        self.flip_bricks(player,row,col)
        self.white_moves = None
        self.black_moves = None
        self.calc_utility()
        return 1

    def calc_utility(self):
        # End-game evaluation function
        if self.starting_depth > 40:
            w, b = 0,0
            for row in range(8):
                for col in range(8):
                    if self.board[row][col] == WHITE:
                        w += 1
                    if self.board[row][col] == BLACK:
                        b += 1
            self.utility = b - w
        # early/mid-game evaluation function
        else:
            self.utility = len(self.find_legal_moves(BLACK)) - len(self.find_legal_moves(WHITE))
            self.utility += self.board[0][0] * 100
            self.utility += self.board[7][0] * 100
            self.utility += self.board[0][7] * 100
            self.utility += self.board[7][7] * 100

    def calc_winner(self):
        winner = 0
        for row in range(8):
            for col in range(8):
                winner += self.board[row][col]
        if winner > 0:
            return "BLACK"
        elif winner < 0:
            return "WHITE"
        else:
            return "DRAW"

    def flip_bricks(self,player,row,col):
        for tup in DIRECTIONS:
            new_row = row + tup[0]
            new_col = col + tup[1]
            bracket = 0
            flip = 0
            while self.within_board(new_row) and self.within_board(new_col):
                if self.board[new_row][new_col] == -player:
                    bracket = 1
                    new_row += tup[0]
                    new_col += tup[1]
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
                    new_row += tup[0]
                    new_col += tup[1]

