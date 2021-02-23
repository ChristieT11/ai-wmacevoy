from typing import List, Tuple, Optional
from agent import Agent
from game import Game
from const import Const
from move import Move
import random

class EdgeGoatAgent(Agent):
    def __init__(self,game : Game, side : int):
        super(EdgeGoatAgent, self).__init__(game,side)
        if side != Const.MARK_GOAT:
            raise ValueError("side must be goat")
    
    def openEdges(self,row : int, col : int):
        game : Game = self.game
        board : List[List[int]] = game.board
        edgesList = [board[0][0],board[0][1],board[0][2],board[0][3],board[0][4],
            board[1][0],board[1][4],board[2][0],board[2][4],board[3][0],board[3][4],
            board[4][0],board[4][1],board[4][2],board[4][3],board[4][4]]
        for (dRow,dCol) in Const.DIRS[(row,col)]:
            for board[row+dRow][col+dCol] in edgesList:
                if edgesList[board[row+dRow][col+dCol]] == Const.MARK_NONE:
                    return True
        return False

    def propose(self) -> Move:
        openEdgesMoves : List[Move] =  []
        moves = self.game.goatMoves()
        for move in moves:
            if self.openEdges(move.toRow,move.toCol):
                openEdgesMoves.append(move)
        if len(openEdgesMoves) > 0:
            return random.choice(openEdgesMoves)    
        if (len(moves) == 0):
            print(self.game)
        return random.choice(moves)
