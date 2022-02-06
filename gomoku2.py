from __future__ import division

from copy import deepcopy
from mcts import mcts
from functools import reduce
import operator

BOARD_SIZE = 15


def checkRow(arr: [str], color):
    cont = 0
    for i in arr:
        if i == color:
            cont += 1
            if cont >= 5:
                return True
        else:
            cont = 0
    return False


class GomokuState:
    def __init__(self):
        self.board = [[0] * BOARD_SIZE for i in range(BOARD_SIZE)]
        self.currentPlayer = 1

    def getCurrentPlayer(self):
        return self.currentPlayer

    def getPossibleActions(self):
        possibleActions = []
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 0:
                    possibleActions.append(Action(player=self.currentPlayer, x=i, y=j))
        return possibleActions

    def takeAction(self, action):
        newState = deepcopy(self)
        newState.board[action.x][action.y] = action.player
        newState.currentPlayer = self.currentPlayer * -1
        return newState

    def getVertRow(self, row: int, col: int):
        vert = []
        for i in range(-4, 5):
            if 0 <= col + i <= 14:
                vert.append(self.board[row][col + i])
        return vert

    def getHorRow(self, row: int, col: int):
        vert = []
        for i in range(-4, 5):
            if 0 <= row + i <= 14:
                vert.append(self.board[row + i][col])
        return vert

    def getDia1Row(self, row: int, col: int):
        vert = []
        for i in range(-4, 5):
            if 0 <= row + i <= 14 and 0 <= col + i <= 14:
                vert.append(self.board[row + i][col + i])
        return vert

    def getDia2Row(self, row: int, col: int):
        vert = []
        for i in range(-4, 5):
            if 0 <= row + i <= 14 and 0 <= col + i <= 14:
                vert.append(self.board[row + i][col + i])
        return vert

    def checkWin(self, color: int, row: int, col: int):
        if checkRow(self.getVertRow(row, col), color) or checkRow(self.getHorRow(row, col), color) \
                or checkRow(self.getDia1Row(row, col), color) or checkRow(self.getDia2Row(row, col), color):
            # print(f"{'Black' if color == 0 else 'White'} Wins!")
            return True
        return False

    def isTerminal(self):
        for i in range(0, BOARD_SIZE):
            for j in range(0, BOARD_SIZE):
                if self.checkWin(-1, i, j) or self.checkWin(1, i, j):
                    return True
        return False

    def getReward(self):
        for i in range(0, BOARD_SIZE):
            for j in range(0, BOARD_SIZE):
                if self.checkWin(-1, i, j):
                    return -1
                if self.checkWin(1, i, j):
                    return 1
        return False


class Action():
    def __init__(self, player, x, y):
        self.player = player
        self.x = x
        self.y = y

    def __str__(self):
        return str((self.x, self.y))

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.x == other.x and self.y == other.y and self.player == other.player

    def __hash__(self):
        return hash((self.x, self.y, self.player))


if __name__ == "__main__":
    initialState = GomokuState()
    searcher = mcts(timeLimit=1000000)
    action = searcher.search(initialState=initialState)

    print(action)
