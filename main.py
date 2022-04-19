import time
import os
import random
from colorama import Fore, init

init()

pos_to_diagonals = {0: (4,), 1: (3, 5), 2: (
    4,), 3: (1, 7), 4: (0, 2, 6, 8), 5: (1, 7), 6: (4,), 7: (3, 5), 8: (4,)}


board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


current_player = 'x'


WAYS_TO_WIN = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
               (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)


def easy_move():
    return random.choice(valid_moves())


def other_player():
    if current_player == 'x':
        return 'o'
    return 'x'


def player():
    print(f'Choose a position {current_player}')
    while True:
        try:
            pos = int(input())
        except ValueError:
            print('You must provide an integer in the range from 1-9')
            continue
        if pos-1 in list(range(9)):
            if check_valid_pos(pos-1):
                return pos-1
            print('Position taken try again')
            print('You must provide an integer in the range from 1-9')


def EXTREME_MODE():
    import time
    time.sleep(0.1)
    b = (0, 4, 8)
    time.sleep(0.5)
    for i in range(2):
        board[b[i]] = current_player
        os.system('clear')
        display_board()
        time.sleep(0.5)
    return 8


def calculate_best_move_hard():
    global board
    board_ = board[:]

    for move in valid_moves():
        board_[move] = current_player
        if check_winner_(board_):
            return move
        board_[move] = ' '

    for way_to_win in WAYS_TO_WIN:
        if board[way_to_win[0]] == board[way_to_win[2]] != ' ':
            if check_valid_pos(way_to_win[1]):
                return way_to_win[1]

        elif board[way_to_win[0]] == board[way_to_win[1]] != ' ':
            if check_valid_pos(way_to_win[2]):
                return way_to_win[2]

        elif board[way_to_win[2]] == board[way_to_win[1]] != ' ':
            if check_valid_pos(way_to_win[0]):
                return way_to_win[0]

    for best_move in BEST_MOVES:
        if check_valid_pos(best_move):
            return best_move


def display_board():
    BORED_DISP = []
    for peice in board:
        if peice == 'x':
            BORED_DISP.append(f'{Fore.YELLOW}x{Fore.RESET}')
        elif peice == 'o':
            BORED_DISP.append(f'{Fore.RED}o{Fore.RESET}')
        else:
            BORED_DISP.append(' ')

    if not ARCHIVE:
        os.system('clear')
    print("\n\t", BORED_DISP[0], "|", BORED_DISP[1], "|", BORED_DISP[2])
    print("\t", "---------")
    print("\n\t", BORED_DISP[3], "|", BORED_DISP[4], "|", BORED_DISP[5])
    print("\t", "---------")
    print("\n\t", BORED_DISP[6], "|", BORED_DISP[7], "|", BORED_DISP[8], "\n")


def calculate_best_move_medium():
    if len(valid_moves()) == 9:
        return 4
    for way_to_win in WAYS_TO_WIN:
        if board[way_to_win[0]] == board[way_to_win[2]] != ' ':
            if check_valid_pos(way_to_win[1]):
                return way_to_win[1]

        elif board[way_to_win[0]] == board[way_to_win[1]] != ' ':
            if check_valid_pos(way_to_win[2]):
                return way_to_win[2]

        elif board[way_to_win[2]] == board[way_to_win[1]] != ' ':
            if check_valid_pos(way_to_win[0]):
                return way_to_win[0]

    xpos = board.index(other_player())

    diagonals_for_x = pos_to_diagonals[xpos]
    for diagonal in diagonals_for_x:
        if check_valid_pos(diagonal):
            return diagonal

    move = board.index(other_player())
    while True:
        move += 1
        if check_valid_pos(move):
            return move


X = calculate_best_move_hard
O = calculate_best_move_hard
DELAY = 0.5
ARCHIVE = False


def check_valid_pos(pos):
    global board

    if board[pos] == ' ':
        return True
    return False


def valid_moves():
    moves = []
    for pos in range(9):
        if board[pos] != ' ':
            continue
        moves.append(pos)
    return moves


def check_winner():
    global board
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != ' ':
            winner = board[row[0]]
            return winner
    if ' ' not in board:
        return 'TIE'
    return None


def check_winner_(board):
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
        pos = X()
        board[pos] = f'{current_player}'

    else:
        move = O()

        board[move] = f'{current_player}'
    if DELAY:
        time.sleep(DELAY)

    if current_player == 'x':
        current_player = 'o'
    else:
        current_player = 'x'
