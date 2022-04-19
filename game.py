import os

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
current_player = 'x'
WAYS_TO_WIN = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),(1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

def player():
    print(f'Choose a position {current_player}')
    while True:
        try:
            pos = int(input())
        except ValueError:
            print('You must provide an integer in the range from 1-9')
            continue
        if pos-1 in list(range(9)):
            if check_valid_pos(pos-1):return pos-1
            print('Position taken try again\nYou must provide an integer in the range from 1-9')
def display_board():
    os.system('clear')
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\n\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\n\t", board[6], "|", board[7], "|", board[8], "\n")

def check_valid_pos(pos):
    global board
    if board[pos] == ' ':
        return True
    return False

def check_winner():
    global board
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != ' ':
            winner = board[row[0]]
            return winner
    if ' ' not in board:
        return 'TIE'
    return None

while True:
    display_board()
    state = check_winner()
    if state == 'TIE':
        print('Tie!')
        break
    elif state == 'x' or state == 'o':
        print(f'{state} won!')
        break
    print("""
    \t1 | 2 | 3
    \t---------
    \t4 | 5 | 6
    \t---------
    \t7 | 8 | 9
    """)
    if current_player == 'x':
        pos = player()
        board[pos] = f'{current_player}'

    else:
        move = player()
        board[move] = f'{current_player}'

    if current_player == 'x':
        current_player = 'o'
    else:
        current_player = 'x'
