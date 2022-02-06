BOARD_SIZE = 15
BOARD = []
PLAYER1COLOR = None
PLAYER2COLOR = None
TURN = 0
EMPTY_SPACE = '+'


def initializeBoard():
    global BOARD
    BOARD = [[0] * BOARD_SIZE for i in range(BOARD_SIZE)]


def printBoard():
    print('\n'.join('  '.join(str((EMPTY_SPACE if x == 0 else x)) for x in row) for row in BOARD))


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
        if 0 <= col + i <= 14:
            vert.append(BOARD[row][col + i])
    return vert


def getHorRow(row: int, col: int):
    vert = []
    for i in range(-4, 5):
        if 0 <= row + i <= 14:
            vert.append(BOARD[row + i][col])
    return vert


def getDia1Row(row: int, col: int):
    vert = []
    for i in range(-4, 5):
        if 0 <= row + i <= 14 and 0 <= col + i <= 14:
            vert.append(BOARD[row + i][col + i])
    return vert


def getDia2Row(row: int, col: int):
    vert = []
    for i in range(-4, 5):
        if 0 <= row + i <= 14 and 0 <= col + i <= 14:
            vert.append(BOARD[row + i][col + i])
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
    if checkRow(getVertRow(row, col), color) or checkRow(getHorRow(row, col), color) \
            or checkRow(getDia1Row(row, col), color) or checkRow(getDia2Row(row, col), color):
        print(f"{'Black' if color == 0 else 'White'} Wins!")
        return True
    return False


def play(color: int, row: int = None, col: int = None):
    global BOARD
    legalPlay = False

    if row is not None and col is not None and 0 <= row <= 14 and 0 <= col <= 14:
        printBoard()
        return checkWin(color, row, col)

    while not legalPlay:
        row = None
        col = None
        while row is None:
            val = input(f"{'Black' if color == 0 else 'White'} enter row (0-14): ")
            try:
                if 0 <= int(val) <= 14:
                    row = int(val)
            except:
                print("Error! Invalid Input!")
                continue

        while col is None:
            val = input(f"{'Black' if color == 0 else 'White'} enter col (0-14): ")
            try:
                if 0 <= int(val) <= 14:
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
    return checkWin(color, row, col)


def main():
    initializeBoard()
    # getBlackWhite()
    printBoard()

    win = False

    while not win:
        global TURN

        if TURN % 2 == 0:
            win = play(0)
        else:
            win = play(1)

        TURN += 1


if __name__ == '__main__':
    main()
