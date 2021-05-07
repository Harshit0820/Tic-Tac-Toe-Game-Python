# MILESTONE PROJECT 1 IN PYTHON :- TIC-TAC-TOE GAME
# OVERVIEW AND QUES ON THE TEXT FILE HERE CODE ONLY
# LET'S START

# 1. Display the board or game
def display_game(board):
    print(
        board[7] + ' | ' + board[8] + ' | ' + board[9] + '\n----------\n' + board[4] + ' | ' + board[5] + ' | ' + board[
            6] + '\n----------\n'
        + board[1] + ' | ' + board[2] + ' | ' + board[3])

test_board = [' ']*10

# 2. Assigning marker to players
def assign_marker():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()
    if marker == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'



# 3. To assign where to put marker
def place_maker(board, marker, position):
    board[position] = marker

# 4. Check for winner
def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            (board[9] == mark and board[6] == mark and board[3] == mark) or
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[9] == mark and board[5] == mark and board[1] == mark))

# 5. Which player goes first
import random
def choose_first():
    num = random.randint(0,1)
    if num == 0:
        return 'Player 1'
    else:
        return 'Player 2'

# 6. Check if position on board is free or not
def space_check(board, position):
    return board[position] == ' '


# 7. To chek if board is full
def check_full(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

# 8. Ask for next position of player's and check if it is free or not
def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
    return position

# 9. Ask for new game
def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

# 10. Final Logic
print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    test_board = [' '] * 10
    player1_marker, player2_marker = assign_marker()
    turn = choose_first()
    print(turn + ' will go first.')

    play_game = input('Are you ready to play? Enter Yes or No: ')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.

            display_game(test_board)
            position = player_choice(test_board)
            place_maker(test_board, player1_marker, position)

            if win_check(test_board, player1_marker):
                display_game(test_board)
                print('Congratulations! Player 1 has won the game!')
                game_on = False
            else:
                if check_full(test_board):
                    display_game(test_board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.

            display_game(test_board)
            position = player_choice(test_board)
            place_maker(test_board, player2_marker, position)

            if win_check(test_board, player2_marker):
                display_game(test_board)
                print('Congratulations! Player 2 has won the game!')
                game_on = False
            else:
                if check_full(test_board):
                    display_game(test_board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break

# Good Job!
