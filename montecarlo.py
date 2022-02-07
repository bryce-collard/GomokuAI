from Gomoku import *
from Metrics import Metrics
from tqdm import tqdm

def get_player_color():
    player_col = None
    while player_col != "B" and player_col != "W":
        if player_col:
            print("Type 'B' for black, or type 'W' for white.")
        player_col = input("Choose a color: (B)lack/(W)hite: ")
    return player_col

def select_board(board, history, player):
   boards = get_possible_moves(board, player)
   for b in boards:
      if str(b) not in history:
         history[str(b)] = Metrics()
   boards.sort(key=lambda b:history[str(b)].get_ucb(player, history[str(board)]))
   boards.reverse()
   return boards[0]

def run_simulations(board, history, player, count=100):
   for i in tqdm(range(count)):
      curr_board = board
      game_path = [curr_board]
      curr_player = player

      if str(curr_board) not in history:
         history[str(curr_board)] = Metrics()

      while get_score(curr_board) is None:
         curr_board = select_board(curr_board, history, curr_player)
         game_path += [curr_board]
         if curr_player == "W":
            curr_player = "B"
         else:
            curr_player = "W"
      result = get_score(curr_board)
      for b in game_path:
         history[str(b)].update(result)


def find_best_move(color, history):
   board = getBoard()
   if str(board) not in history:
      history[str(board )] = Metrics()
   print("Deciding best move...")
   run_simulations(board, history, color, count=500)
    # boards = get_possible_moves(board, player)
    # values = [history[b.tostring()].get_expected_value(player) for b in boards]
    # return boards[np.argmax(values)]


def play_game():
    global BOARD

    player_color = get_player_color()
    ai_color = "W" if player_color == "B" else "B"
    history = {}
    initializeBoard()
    printBoard()

    win = False
    turn = 0
    while not win:
        if turn % 2 == 0:
            if player_color == "B":
                win = play(0)
            else:
                find_best_move(ai_color, history)
        else:
            if player_color == "W":
                win = play(1)
            else:
                find_best_move(ai_color, history)
        turn += 1


if __name__ == "__main__":
    play_game()
