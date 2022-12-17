from time import sleep  # welcome message animation
import random  # for computers move
import sys  # to access parameters and functions

welcome_message = "Welcome to the Tic Tac Toe game!\n"

for x in welcome_message:
    print(x, end='')
    sys.stdout.flush()
    sleep(.2)

player_move  = 'X'
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
winner = None
name = None
x_score = 0
o_score = 0


game_instructions = '''

Read instructions to play the game: \n
- The game displays a 3X3 grid
- The user(you) will start the game first with the letter 'X'
- The computer (opposition) will follow by the letter 'O'
- To place your letter type a number between 1-9 this will choose your position
- The first display their letter ('X', 'O') horizontally, vertically or diagonally wins!
- If all of the 9 spaces are full and no one has won, the game will end in a draw
'''
print(game_instructions)

def player_name():
    '''
    Gets players name and only accpeting letters
    '''
    while True:
        global name 
        name = input("\nPlease enter your name\n").capitalize()

        if name.isalpha():
            print("\n")
            print(f"Hi{name} Welcome to Tic Tac Toe!")
            print(game_instructions)

            break

        else:
            print("Invalid input, only letters accepted.")
            print("Please try again.")

    player_name()

    def start_game():
        '''
        asks the user to enter 'S' so the game can start
        '''
        while True:
            start_game_input = input("Type 'S' to start the game:\n").lower()
            if start_game_input == 's':
                game_starting = 'Game starting...'
                print(game_starting, end="\r")
                time.sleep(1)
                print(" " * len(game_starting), end="\r")
                time.sleep(1)
                break
            else:
                print(f"{start_game_input} Incorrect input, press 'S' to start game.")