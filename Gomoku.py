BOARD_SIZE = 6
BOARD = []
PLAYER1COLOR = None
PLAYER2COLOR = None
TURN = 0
EMPTY_SPACE = '+'


def get_score(board, player, last_row_played, last_col_played, depth=0):
    #checkWin(color: int, row: int, col: int)
    if last_row_played is None:
        # no moves yet; unfinished game
        return None
    playerInt = 0 if player == "B" else 1
    oppPlayerInt = 1 if player == "B" else 0
    # if last_row_played == 5 and last_col_played == 9:
    #     print(last_row_played, last_col_played)
    #     print(playerInt, oppPlayerInt)
    #     print(checkWinWithBoard(board, playerInt, last_row_played, last_col_played))
    #     print(checkWinWithBoard(board, oppPlayerInt, last_row_played, last_col_played))
    if checkWinWithBoard(board, playerInt, last_row_played, last_col_played):
        # player Victory
        return 1 * (1 / (1 + depth))
    elif checkWinWithBoard(board, oppPlayerInt, last_row_played, last_col_played):
        # opponent victory
        return -1 * (1 / (1 + depth))
    else:
        # Unfinished Game
        return None

def getBoard():
    return BOARD

def setBoard(board):
    global BOARD
    BOARD = board

def initializeBoard():
    global BOARD
    BOARD = [[0] * BOARD_SIZE for i in range(BOARD_SIZE)]


def printBoard():
    print('\n'.join('  '.join(str((EMPTY_SPACE if x == 0 else x)) for x in row) for row in BOARD))

def printThisBoard(board):
    print('\n'.join('  '.join(str((EMPTY_SPACE if x == 0 else x)) for x in row) for row in board))

def getBlackWhite():
    global PLAYER1COLOR
    global PLAYER2COLOR

    while PLAYER1COLOR is None:
        val = input("Player 1 enter color (0 for black [first], 1 for white [second]): ")
        if int(val) == 0 or int(val) == 1:
            PLAYER1COLOR = int(val)

    # Player 2 gets other color
    PLAYER2COLOR = (int(val) + 1) % 2


def getVertRow(row: int, col: int):
    vert = []
    for i in range(-4, 5):
        if 0 <= col + i <= BOARD_SIZE - 1:
            vert.append(BOARD[row][col + i])
    return vert

def getVertRowWithBoard(board, row: int, col: int):
    vert = []
    for i in range(-4, 5):
        if 0 <= col + i <= BOARD_SIZE - 1:
            vert.append(board[row][col + i])
    return vert


def getHorRow(row: int, col: int):
    vert = []
    for i in range(-4, 5):
        if 0 <= row + i <= BOARD_SIZE - 1:
            vert.append(BOARD[row + i][col])
    return vert

def getHorRowWithBoard(board, row: int, col: int):
    vert = []
    for i in range(-4, 5):
        if 0 <= row + i <= BOARD_SIZE - 1:
            vert.append(board[row + i][col])
    return vert


def getDia1Row(row: int, col: int):
    vert = []
    for i in range(-4, 5):
        if 0 <= row + i <= BOARD_SIZE - 1 and 0 <= col + i <= BOARD_SIZE - 1:
            vert.append(BOARD[row + i][col + i])
    return vert

def getDia1RowWithBoard(board, row: int, col: int):
    vert = []
    for i in range(-4, 5):
        if 0 <= row + i <= BOARD_SIZE - 1 and 0 <= col + i <= BOARD_SIZE - 1:
            vert.append(board[row + i][col + i])
    return vert


def getDia2Row(row: int, col: int):
    vert = []
    for i in range(-4, 5):
        if 0 <= row + i <= BOARD_SIZE - 1 and 0 <= col + i <= BOARD_SIZE - 1:
            vert.append(BOARD[row + i][col + i])
    return vert

def getDia2RowWithBoard(board, row: int, col: int):
    vert = []
    for i in range(-4, 5):
        if 0 <= row + i <= BOARD_SIZE - 1 and 0 <= col + i <= BOARD_SIZE - 1:
            vert.append(board[row + i][col + i])
    return vert


def checkRow(arr: [str], color):
    cont = 0
    for i in arr:
        if i == ('B' if color == 0 else 'W'):
            cont += 1
            if cont >= 5:
                return True
        else:
            cont = 0
    return False


def checkWin(color: int, row: int, col: int):
    #if row == 5 and col == 9:
        #print(getVertRow(row, col))
    if checkRow(getVertRow(row, col), color) or checkRow(getHorRow(row, col), color) \
            or checkRow(getDia1Row(row, col), color) or checkRow(getDia2Row(row, col), color):
        print(f"{'Black' if color == 0 else 'White'} Wins!")
        return True
    return False

def checkWinWithBoard(board, color: int, row: int, col: int):
    #if row == 5 and col == 9:
        #print(getVertRow(row, col))
    if checkRow(getVertRowWithBoard(board, row, col), color) or checkRow(getHorRowWithBoard(board, row, col), color) \
            or checkRow(getDia1RowWithBoard(board, row, col), color) or checkRow(getDia2RowWithBoard(board, row, col), color):
        #print(f"{'Black' if color == 0 else 'White'} Wins!")
        return True
    return False


def play(color: int, row: int = None, col: int = None):
    global BOARD
    legalPlay = False

    if row is not None and col is not None and 0 <= row <= BOARD_SIZE - 1 and 0 <= col <= BOARD_SIZE - 1:
        printBoard()
        return checkWin(color, row, col)
    while not legalPlay:
        row = None
        col = None
        while row is None:
            val = input(f"{'Black' if color == 0 else 'White'} enter row (0-{BOARD_SIZE - 1}): ")
            try:
                if 0 <= int(val) <= BOARD_SIZE - 1:
                    row = int(val)
            except:
                print("Error! Invalid Input!")
                continue

        while col is None:
            val = input(f"{'Black' if color == 0 else 'White'} enter col (0-{BOARD_SIZE - 1}): ")
            try:
                if 0 <= int(val) <= BOARD_SIZE - 1:
                    col = int(val)
            except:
                print("Error! Invalid Input!")
                continue

        if BOARD[row][col] == 0:
            BOARD[row][col] = 'B' if color == 0 else 'W'
            legalPlay = True
        else:
            print("Error! Space Occupied!")

    printBoard()
    return checkWin(color, row, col), row, col


def main():
    initializeBoard()
    # getBlackWhite()
    printBoard()

    win = False

    while not win:
        global TURN

        if TURN % 2 == 0:
            win = play(0)[0]
        else:
            win = play(1)[0]

        TURN += 1


if __name__ == '__main__':
    main()
