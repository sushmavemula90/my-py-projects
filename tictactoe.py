def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    return False

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def tic_tac_toe():
    board = [[" "," "," "],[" "," "," "],[" "," "," "]]
    players = [{"name": "Player 1", "symbol": "0"}, {"name": "Player 2", "symbol": "X"}]
    current_player = 0
    print("Welcome to Tic Tac Toe!")
    print_board(board)
    while True:
        player = players[current_player]
        row = input(f"{player['name']}, enter row (0, 1, or 2): ")
        col = input(f"{player['name']}, enter column (0, 1, or 2): ")
        if not (row.isdigit() and col.isdigit()):
            print("Please enter valid integers.")
            continue
        row = int(row)
        col = int(col)
        if row not in range(3) or col not in range(3):
            print("Please enter valid indices (0, 1, or 2).")
            continue
        if board[row][col] == " ":
            board[row][col] = player['symbol']
            print_board(board)
            if check_winner(board):
                print(f"{player['name']} wins!")
                break
            elif all(col != " " for row in board for col in row):
                print("Draw!")
                break
            current_player = 1 - current_player
        else:
            print("That position is already taken. Try again.")

tic_tac_toe()
