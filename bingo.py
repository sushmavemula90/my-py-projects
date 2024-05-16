import random
def generate_table():
    numbers = list(range(1, 26))
    table = []
    for i in range(5):
        row = random.sample(numbers, 5)
        table.append(row)
        for num in row:
            numbers.remove(num)
    return table
def print_board(board):
    for row in board:
        print(" | ".join(str(num) for num in row))
def mark_number(board, number, other_board, count):
    for i in range(5):
        for j in range(5):
            if board[i][j] == number:
                if board[i][j] != 'X':
                    board[i][j] = 'X'
                    mark_number_in_other_board(board, number)
                    return check_equality(board)  
                else:
                    print("Number already chosen")
                    return count  
    return count
def mark_number_in_other_board(board, number):
    for i in range(5):
        for j in range(5):
            if board[i][j] == number:
                board[i][j] = 'X'
def check_equality(board):
    count = 0
    for i in range(5):
        if all(cell == 'X' for cell in board[i]):
            count += 1
        if all(board[j][i] == 'X' for j in range(5)):
            count += 1
    if all(board[i][i] == 'X' for i in range(5)):
        count += 1
    if all(board[i][4-i] == 'X' for i in range(5)):
        count += 1
    return count
def play_bingo():
    board1 = generate_table()
    board2 = generate_table()
    count1 = 0
    count2 = 0
    current_player = 1
    while True:
            print("Table 1:")
            print_board(board1)
            print("\nTable 2:")
            print_board(board2)
            number = int(input(f"player {current_player }; choose a number 1-25: "))
            if number < 1 or number > 25:
                number = int(input(f"player {current_player}; choose a different number (1-25): "))
            if current_player == 0:
                count1 = mark_number(board1, number, board2, count1)
            if count1 == 5:
                print("Player 1 wins")
                break
            else:
                count2 = mark_number(board2, number, board1, count2)
            if count2 == 5:
                print("Player 2 wins")
                break
            if current_player==1:
                current_player=2
            else:
                curent_player=1

play_bingo()
