# Portfolio project - 3 Python

# Tic Tac Toe

Tic Tac Toe is a python terminal game, which runs in the Code Institute mock terminal on Heroku

## Introduction

Tic Tac Toe is a game where two players each take turns in choosing either an 'X' or an 'O' in one square of a grid consisting of nine squares, in this case the game is against the computer. The first player who gets 3 of the same letters('X' or 'O') wins the game this is achieved by having the same letters in horizontally, vertically or diagonally.

[Here is the live version of my project:](https://python-tic-tac-toe.herokuapp.com/)

[Here is a link to my GitHub repository:](https://github.com/AdamRalph123/tic-tac-toe)

![AmIResponsive](images/responsive.png)


# Table of contents
1. [Features](#features)
    * [Run programme](#run-programme)
    * [Name input](#name-input)
    * [Start game](#start-game)
    * [Check win](#check-win)
    * [Check tie](#check-tie)
    * [Game over](#game-over)
    * [Invalid input](#invalid-input)
2. [User stories](#user-stories)
3. [Technology used](#technology-used)
4. [Testing](#testing)
5. [Bugs](#bugs)
6. [Future Features](#future-features)
7. [Deployment](#deployemnt)
8. [Credits](#credits)
9. [Acknowledgement](#acknowledgement)


# Features

## Run programme
when the user runs the progremme a welcome message will be shown, I uesed the sleep method so that the welcome message appears word by word. The game instructions appear so the user will know how to play the game and also a mock up board so the user will know how to input their chosen letter('X' or 'O').

![screenshot](images/program.run.png)


## Name input
The user will be asked what their name is, letters will only be accepted as seen below.

![screenshot](images/name.input.png)


## Start game 
After the user has entered their name a welcome message will appear and it will ask the user to type 'S' to start the game, a loading message will then appear saying 'game starting', the game board will then appear and ready for the user to play.

![screenshot](images/start.game.png)


## Check win
If the user has won the game a message will appear saying 'you are the winner' if the computer has won it will say 'Oops the computer has won' and the game will the end.

![screenshot](images/check-win1.png)
![screenshot](images/check-win2.png)


## Check tie
If thr user or the computer has not won thr game will end in a tie and a message will appear saying 'its a tie' and the game will end. If the user has picked a spot thats already taken it will let the usre know and they will have to choose a differnt spot.

![screenshot](images/check-tie.png)
![screenshot](images/different-spot.png)


## Game over
After the ended in a win or tie a game over message will appear and it will ask the user if the want to quit the game, when pressed a thank you message will appear.

![screenshot](images/game-over.png)

## Invalid input
If the user enters a letter when asked to enter a number 1-9 a message will appear saying 'Oops invalid input. Please enter a valid number.

If the user enters a number thats not between 1-9 and message will appear saying 'Invalid selection. Number must be between 1-9

![screenshot](images/invalid-input.png)


# User stories
As a player:
* I want to play a game with clear and easy instructions.
* I want a working game.
* I want messages to appear if i win, lose or tie.


# Technology used 
* Python
* JavaScript provided in the Code Institute Template
* HTML provided in the Code Institute Template


# Testing
Testing was conducted through out my entire project. Pep8 validator came back with no issues.

![screenshot](images/PEP8CI.png)


# Bugs 
I had a bug in my code when playing the game, if I won the game with enetering 3 inputs, the board would only show 2 inputs instead of three, I fixed this bug by adding print_board(board) in my check_win function.


# Future features
If was to make this game again I would add a scoreboard so the user can keep track of their score and I would also add a timer to make the game more intense.


# Deployment
The project was developed through Gitpod using the template provided by Code Institute.

The is made using [Heroku](https://www.heroku.com/) the steps are listed below

1. Login or register on Heroku.
2. Click on 'new' in the dashboard and select 'create new app'.
3. Select a name for your app and choose your region.
4. Click on 'create new app'
5. To improve compatibility with various python libraries add Config Var with Key = Port
and the Value = 8000.
6. Add 2 buildpacks: Python and the Nodejs in that order.
7. Go back to the top and click on 'Deploy' and select 'Github'.
8. Scroll down and click on 'Connect to Github'.
9. Go back at the top and click on 'Deploy' and select 'GitHub'.
10. Scroll down and click on 'Connect to GitHub'.
11. Search for your GitHub repository name by typing it.
12. Click on 'Connect'.
Scroll down and click on 'Deploy Branch'.
13. You will see a message saying 'The app was successfully deployed' when the app is built with python and all the depencenies.





# Credits 
<u>YouTube</u>

Some of my code was done by watching YouTube tutorials from (https://www.youtube.com/@CodeCoachh)

<u>Research</u>

(https://www.w3schools.com/) helped me with my research and understanding.


 # Acknowledgement
 I would like to thank;
 
 * My mentor [Jubril Akolade](https://www.linkedin.com/in/jubrillionaire/) who is always there for support and to answer any questions i have for him.
 * The slack community (https://slack.com/intl/en-ie/https://slack.com/intl/en-ie/) which i can always rely on.
 * I would like to thank the assessment team for taking their time to look over my project.
