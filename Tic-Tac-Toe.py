#display_instruct()函数
def display_instruct():
    """Display game instructions."""
    print(
    """
    welcome to the greatest intellectual challenge of all time:Tic-Tac-Toe.
    This will be a showdown between your human brain and my silicon processor.

    You will make your move known by entering a number, 0 - 8. The number
    will correspond to the board position as illustrated:
                0 | 1 | 2
                ---------
                3 | 4 | 5
                ---------
                6 | 7 | 8

    perpare yourself, human. The ultimate battle is about to begin.\n
    """
    )

#ask_yes_no()函数
def ask_yes_no(question):
    """Ask a yes or no question."""
    response = None
    while response not in("y", "n"):
        response = input(question).lower()
    return response

#ask_number（）函数
def ask_number(question, low, high):
    """Ask for a number within a range."""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

#pieces()函数
#该函数询问玩家是否有希望先行棋
def pieces():
    """Determine if player or computer goes first."""
    go_first = ask_yes_no("Do you require the first move? (y/n):")
    if go_first == "y":
        print("\nThen take the first move. You will need it.")
        human = X
        computer = 0
    else:
        print("\nYour bravery will be your undoing... I will go first.")
        computer = X
        human = 0
    return computer, human

#new_board函数
#该函数用于创建新棋盘
def new_board():
    """Create new game board."""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

#display_board函数
#显示棋盘，打印“X","O"元素
def display_board(board):
    """Display game board on screen."""
    print("\n\t", board[10], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")

#legal_moves函数
#确保玩家选择的是一步合法的棋
def legal_moves(board):
    """Create list of legal moves."""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves
#winner函数
#判断输赢
def winner(board):
    """Determine the game winner."""
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6),

    for row in WAYS_TO_WIN:
         if board[row[0]] == board[row[1]] != EMPTY:
             winner = board[row[0]]
            return winner
    if EMPTY not in board:
            return None

#human_move函数
def human_move(board, human):
    """Get human move.""'
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Where will you move? (0 - 8):", 0, NUM_SQUQRES)
        if move not in legal:
           print("\nThat square is alreagy occupied, foolish huamn.Choose
another.\n")
    print("Fine...")
    return move


