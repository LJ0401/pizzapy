#computer_move()函数
def computer_move(board, computer, human):
    """Make computer move."""
    #该函数会修改列表，需要创建一个副本
    board = board[:]

#next_turn()函数
def next_turn(turn):
    """Switch turns."""
    if turn == X:
        return O
    else:
        return X
#congrat_vinter()函数，只在游戏结束时被调用
def congrat_winner(the_winner, computer, human):
    """Congratulate the winner."""
    if the_winner != TIE:
        print(the_winner, "won!\n")
    else:
        print("It's a tie!\n")

    if the_winner == computer:
        print("As I predicted, human, I am triumphant once more. \n"
              "Proof that computers are superior to humans in all regrads.")

    elif the_winner == human:
        print("NO, no! It cannot be! Somehow you tricked me, human. \n"
              "But never again! I, the computer, so swear it!")

    elif the_winner == TIE:
        print("You were most lucky, human, and somehow mangaed to tie me. \n"
              "Celebrate today...for this is the best you will ever achieve.")

#主程序
def main():
    display_instruct()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)

    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)

    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)
#启动程序
main()
input("\n\nPress the enter key to quit.")
