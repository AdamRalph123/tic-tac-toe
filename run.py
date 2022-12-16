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
- If all of the 9 spaces are full and no one has won the game will end in a draw
'''