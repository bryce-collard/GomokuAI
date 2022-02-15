from stat import SF_IMMUTABLE
from Gomoku import *
from Metrics import Metrics
from tqdm import tqdm
import numpy as np

def get_player_color():
    player_col = None
    while player_col != "B" and player_col != "W":
        if player_col:
            print("Type 'B' for black, or type 'W' for white.")
        player_col = input("Choose a color: (B)lack/(W)hite: ")
    return player_col

def get_possible_moves(board, player):
    # possible moves for 'player'
    possible_moves = []
    for i, row in enumerate(board):
        for j, entry in enumerate(row):
            if entry == 0:
                new_board = [row[:] for row in board]
                new_board[i][j] = player
                possible_moves.append((new_board, i, j))
    return possible_moves

def select_board(board, history, player):
   # boards = [(board, row, col), (board, row, col) ...]
   boards = get_possible_moves(board, player)
   for b in boards:
      if str(b[0]) not in history:
         history[str(b[0])] = Metrics()
   if len(boards) == 0:
       # no moves, tie game
       return None, None, None
   boards.sort(key=lambda b:history[str(b[0])].get_ucb(player, history[str(board)]))
   boards.reverse()
   return boards[0]

def run_simulations(board, history, player, last_row_played, last_col_played, count=100):
   simulated_next_moves = []
   for _ in tqdm(range(count)):
      curr_board = board
      game_path = [curr_board]
      curr_player = player

      if str(curr_board) not in history:
         history[str(curr_board)] = Metrics()

      first = True
      while get_score(curr_board, player, last_row_played, last_col_played) is None:
         curr_board, last_row_played, last_col_played = select_board(curr_board, history, curr_player)
         if first:
             first = False
             if curr_board not in simulated_next_moves:
                 #print(len(simulated_next_moves))
                 simulated_next_moves.append(curr_board)
         if curr_board == None:
             #tie game
             break
        #  print("-------------")
        #  printThisBoard(curr_board)
         game_path += [curr_board]
         if curr_player == "W":
            curr_player = "B"
         else:
            curr_player = "W"
      #print(curr_board)
      if curr_board == None:
          # tie game
          result = 0
      else:
          result = get_score(curr_board, player, last_row_played, last_col_played)
      for b in game_path:
         history[str(b)].update(result)
   #print(len(simulated_next_moves))
   return simulated_next_moves


def find_best_move(color, history, last_row_played, last_col_played):
   board = getBoard()
   print(board)
   if str(board) not in history:
      history[str(board)] = Metrics()
   print("Deciding best move...")
   simulated_moves = run_simulations(board, history, color, last_row_played, last_col_played, count=1000)
   values = [history[str(sm)].get_expected_value(color) for sm in simulated_moves]
   #print([printThisBoard(sm) for sm in simulated_moves])

   boards = get_possible_moves(board, color)
   values2 = [history[str(b[0])].get_expected_value(color) for b in boards]

   print(values2)
   return boards[np.argmax(values2)][0]
   #return simulated_moves[np.argmax(values)]

def TEMP_find_best_move(board, color, history, last_row_played, last_col_played):
   if str(board) not in history:
      history[str(board)] = Metrics()
   print("Deciding best move...")
   simulated_moves = run_simulations(board, history, color, last_row_played, last_col_played, count=1000)
   values = [history[str(sm)].get_expected_value(color) for sm in simulated_moves]
   #print([printThisBoard(sm) for sm in simulated_moves])

   boards = get_possible_moves(board, color)
   values2 = [history[str(b[0])].get_expected_value(color) for b in boards]

   print(values2)
   return boards[np.argmax(values2)][0]
   #return simulated_moves[np.argmax(values)]


def play_game():
    #global BOARD

    player_color = get_player_color()
    ai_color = "W" if player_color == "B" else "B"
    history = {}
    initializeBoard()
    printBoard()

    win = False
    turn = 0
    rowplayed = colplayed = None
    while not win:
        if turn % 2 == 0:
            if player_color == "B":
                win, rowplayed, colplayed = play(0)
            else:
                move = find_best_move(ai_color, history, rowplayed, colplayed)
                setBoard(move)
                printBoard()
        else:
            if player_color == "W":
                win, rowplayed, colplayed = play(1)
            else:
                move = find_best_move(ai_color, history, rowplayed, colplayed)
                setBoard(move)
                printBoard()
        turn += 1


if __name__ == "__main__":
    play_game()

    # history = {}
    # temp = [[0, 'W', 0, 'B', 'B', 'B'],
    #         [0, 0, 'W', 0, 'B', 'W'],
    #         [0, 0, 0, 'B', 0, 'W'],
    #         [0, 0, 'B', 0, 0, 'W'],
    #         [0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0]]
    # move = TEMP_find_best_move(temp, 'W', history, 3, 2)
    # setBoard(move)
    # printBoard()
