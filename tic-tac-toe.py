import random
def print_board(board):
    for row in board:
        print(" | ".join(row)) 
        print("-" * 5)
def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or \
       board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False
def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    print("You are X, computer is O")
    print_board(board)
    while True:
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter col (0-2): "))
        if board[row][col]!=" ":
            print("Cell taken. Try again.")
            continue
        board[row][col]="X"
        print_board(board)
        if check_winner(board,"X"):
            print("You win")
            break
        if not get_empty_cells(board):
            print("It's a draw")
            break
        r,c = random.choice(get_empty_cells(board))
        board[r][c] ="O"
        print("Computer moved:")
        print_board(board)
        if check_winner(board,"O"):
            print("Computer wins")
            break
        if not get_empty_cells(board):
            print("It's a draw")
            break
tic_tac_toe()
