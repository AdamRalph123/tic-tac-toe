from time import sleep  # welcome message animation
import sys  # to access parameters and functions
import random  # computers turn

welcome_message = "Welcome to the Tic Tac Toe game!\n"

for x in welcome_message:
    print(x, end='')
    sys.stdout.flush()
    sleep(.1)

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
winner = None
name = None
current_player = "X"
game_running = True


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

    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])


def player_input(board):
    inp = int(input("Enter a number 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = current_player
    else:
        print("Oops player is in that spot!")
        switch_player()


def check_row(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True


def check_diagonally(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True


def check_horizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True


def check_tie(board):
    global game_running
    if "-" not in board:
        print_board(board)
        print("It is a tie!")
        game_running = False

        return_to_main_page()


def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"


# computer
def computer(board):
    while current_player == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switch_player()


def check_win(board):
    if check_row(board) or check_diagonally(board) or check_horizontal(board):
        print(f"The winner is {winner}")

        return_to_main_page()


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


while game_running:
    print_board(board)
    player_input(board)
    check_win(board)
    check_tie(board)
    switch_player()
    computer(board)
    check_tie(board)
