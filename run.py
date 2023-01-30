'''imports'''
from time import sleep  # welcome message animation
import sys  # to access parameters and functions
import random  # computers turn
import time # for game starting game statement to disappear after a few seconds

# welcome title with animation
welcome_message = "Welcome to the Tic Tac Toe game!\n"

for x in welcome_message:
    print(x, end='')
    sys.stdout.flush()
    sleep(.1)

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
winner = None
name = None
current_player = "X"


# print game instructions
game_instructions = '''

Please read instructions to play the game: \n
- The game displays a 3X3 grid
- The user(you) will start the game first with the letter 'X'
- The computer (opposition) will follow by the letter 'O'
- To place your letter type a number between 1-9 this will choose your position
- The first display their letter ('X', 'O')
  horizontally, vertically or diagonally wins!
- If all of the 9 spaces are full and no one has won,
  the game will end in a tie

                           1 | 2 |  3
                          ------------
                           4 | 5  | 6
                          ------------
                           7 | 8  | 9
                           '''
print(game_instructions)


# players name input
def get_name():
    '''
    Gets players name and only accpeting letters.
    '''
    print("What is your name?")
    while True:
        name = input("My name is: ")
        if not name.isalpha():
            print("Please enter letters only.")
            continue

        else:
            print(f"Welcome {name}!")
            break
    return name


get_name()


def start_game():
    '''
    asks the user to enter 's' so the game can start
    '''
    while True:
        start_game_input = input("Type 'S' to start the game:\n").lower()
        if start_game_input == 's':
            game_starting = 'Game starting...'
            print(game_starting, end="\r")
            sleep(1)
            print(" " * len(game_starting), end="\r")
            sleep(1)
            break
        else:
            print(f"{start_game_input}Incorrect input, press 'S' to start game.")


start_game()


def print_board(board):
    '''
    tic tac toe board
    '''

    print(board[1], " | ", board[2], " | ", board[3], " | ",)
    print('-'*15)
    print(board[4], " | ", board[5], " | ", board[6], " | ",)
    print('-'*15)
    print(board[7], " | ", board[8],  " | ", board[9], " | ",)
    print('\n')


# checking possible winning options
def check_row(board):
    '''
    checks for possible row win
    '''
    global winner
    if board[1] == board[2] == board[3] and board[1] != ' ':
        winner = board[1]
        return True
    elif board[4] == board[5] == board[6] and board[4] != ' ':
        winner = board[4]
        return True
    elif board[7] == board[8] == board[9] and board[9] != ' ':
        winner = board[7]
        return True


def check_diagonally(board):
    '''
    checks for possible diagonal win
    '''
    global winner
    if board[1] == board[5] == board[9] and board[9] != ' ':
        winner = board[1]
        return True
    elif board[3] == board[5] == board[7] and board[7] != ' ':
        winner = board[3]
        return True


def check_colum(board):
    '''
    checks for possible vertical win
    '''
    global winner
    if board[1] == board[4] == board[7] and board[1] != ' ':
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[8] != ' ':
        winner = board[2]
        return True
    elif board[3] == board[6] == board[9] and board[9] != ' ':
        winner = board[3]
        return True


def check_tie(board):
    '''
    checks for a tie, prints a message to let the user know
    '''
    if board.count(' ') > 1:
        return False
    else:
        return True


# switching player 'X' to computer 'O'
def switch_player():
    '''
    switches the player after users move
    '''
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"


# computer
def computer(board):
    '''
    chooses random move for computers move
    '''
    while current_player == "O":
        position = random.randint(1, 9)
        if board[position] == ' ':
            board[position] = "O"
            switch_player()


# check to see who the winner is
def check_win(board):
    '''
    checks for the winner or a tie
    '''
    if check_row(board) or check_diagonally(board) or check_colum(board):
        print_board(board)
        if winner == 'X':
            print("You are the winner!")
        elif winner == 'O':
            print("Oops the computer has won")

        return_to_main_page()

    elif check_tie(board):
        print_board(board)
        print("It's a Tie")
        return_to_main_page()
    else:
        return None


def return_to_main_page():
    '''
    Asks users if they want to quit
    '''
    print("*** Game Over *** \n")

    print("Enter 'q' if you want to quit the game \n")
    while True:
        global name
        make_a_choice = input().strip()
        if make_a_choice.lower() == 'q':
            print(f"Thank you for playing Tic Tac Toe.")
            quit()


def player_input():
    '''
    checks users choice on the board
    '''

    while True:

        print_board(board)

        while True:

            try:

                user_input = int(input("Enter a number 1-9: "))
                if user_input in range(1, 10):
                    if board[user_input] == ' ':
                        board[user_input] = current_player
                        break      
                    else:
                        print(f"Oops player is in that spot!")

                else:
                    print("Invalid selection. Number must be between 1-9")

            except ValueError:
                print("Oops invalid input. Please enter a valid number")

        check_win(board)
        check_tie(board)
        switch_player()
        computer(board)
        check_win(board)
        check_tie(board)


player_input()