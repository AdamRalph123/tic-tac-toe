from time import sleep  # welcome message animation
import sys  # to access parameters and functions
import random

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
currentPlayer = "X"
gameRunning = True


game_instructions = '''

Please read instructions to play the game: \n
- The game displays a 3X3 grid
- The user(you) will start the game first with the letter 'X'
- The computer (opposition) will follow by the letter 'O'
- To place your letter type a number between 1-9 this will choose your position
- The first display their letter ('X', 'O') horizontally, vertically or diagonally wins!
- If all of the 9 spaces are full and no one has won, the game will end in a tie
'''
print(game_instructions)


def get_name():
    '''
    Gets players name and only accpeting letters.
    '''
    print("What is your name?")
    while True:
        name = input("\nMy name is: ")
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
    asks the user to enter 'S' so the game can start
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


def printBoard(board):

    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])


def playerInput(board):
    inp = int(input("Enter a number 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("Oops, that spot is already taken")


def checkRow(board):
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


def checkDiagonally(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
    

def checkHorizontal(board):
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


def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("It is a tie!")
        gameRunning = False

def checkWin():
    if checkRow(board) or checkDiagonally(board) or checkHorizontal(board):
        print(f"The winner is{winner}")

def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"


# computer
def computer(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()


def clear_board():
    '''
    Clears the board if user wants to play again
    '''
    board.extend([" ", " ", " ", " ", " ", " ", " ", " ", " "])
    board.clear()


def return_to_main_page():
    '''
    Asks users if they want to play again or quit
    '''
    print("*** Game Over *** \n")

    print("Enter 'P' to play again \n")
    print("Enter 'Q' if you want to quit the game \n")
    while True:
        global name
        make_a_choice = input().strip()
        if make_a_choice.lower() == 'q':
            


while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
    computer(board)
    checkWin()
    checkTie(board)
