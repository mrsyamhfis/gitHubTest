#  A simple Tic-Tac-Toe game
# Players 'X' and 'O' take turn inputing their position on the command line using numbers 1-9
# 1 | 2 | 3
# ---------
# 4 | 5 | 6
# ---------
# 7 | 8 | 9
#


# The Game Board 




import random
from turtle import position

board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}

# TODO: update the gameboard with the user input
def markBoard(position, mark):
    position = int(position)
    board[position] = mark
    


# TODO: print the game board as described at the top of this code skeleton
# Will not be tested in Part 1
def printBoard():
    tempBoard = {
        1: '1', 2: '2', 3: '3',
        4: '4', 5: '5', 6: '6',
        7: '7', 8: '8', 9: '9'
    }
    for k in board.keys():
        if board[k] != ' ':
            tempBoard[k] = board[k]

    p = '|'
    q = ' '
    print('     ')
    print(q, tempBoard[1], p, tempBoard[2], p, tempBoard[3])
    print('------------')
    print(q, tempBoard[4], p, tempBoard[5], p, tempBoard[6])
    print('------------')
    print(q, tempBoard[7], p, tempBoard[8], p, tempBoard[9])
    print('     ')


# TODO: check for wrong input, this function should return True or False.
# True denoting that the user input is correct
# you will need to check for wrong input (user is entering invalid position) or position is out of bound
# another case is that the position is already occupied
def validateMove(position):
    position = int(position)
    if position >=1 and position <= 9 and board[position] == ' ':
        return True
    else:
        return False

# TODO: list out all the combinations of winning, you will neeed this
# one of the winning combinations is already done for you
winCombinations = [
    #horizontal
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    #vertical
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    #vertical
    [3, 5, 7],
    [1, 5, 9]

]

# TODO: implement a logic to check if the previous winner just win
# This method should return with True or False
def checkWin(player):
    for combination in winCombinations:

       if board[combination[0]] == player and board[combination[1]] == player and board[combination[2]] == player:
           return True

    return False 


# TODO: implement a function to check if the game board is already full
# For tic-tac-toe, tie bascially means the whole board is already occupied
# This function should return with boolean
def checkFull():
    for v in board.values():

        if v == ' ':
            return False

    return True

def restartGame():
    print ("Do you want to play again?: yes/no")
    reset = input()

    global board
    global gameEnded

    while(reset):
        if reset.lower() == 'yes':
            board = {
                1: ' ', 2: ' ', 3: ' ',
                4: ' ', 5: ' ', 6: ' ',
                7: ' ', 8: ' ', 9: ' '
            }
            gameEnded = False
            break
        elif reset.lower() == 'no':
            print ('Thanks for playing..')
            gameEnded = True
            break
        else:
            print('Invalid input! Please try again and choose from the selection:')
            print("Do you want to play again?: yes/no ")
            reset = input()

def computer():
    while currentTurnPlayer == 'O':
        position = random.randint(0, 8)
        if board[position] == ' ':
            board[position] = 'O'
        
        


#########################################################
## Copy all your code/fucntions in Part 1 to above lines
## (Without Test Cases)
#########################################################

gameEnded = False
currentTurnPlayer = 'X'

# entry point of the whole program
print('Game started: \n\n' +
    ' 1 | 2 | 3 \n' +
    ' --------- \n' +
    ' 4 | 5 | 6 \n' +
    ' --------- \n' +
    ' 7 | 8 | 9 \n')

# TODO: Complete the game play logic below
# You could reference the following flow
# 1. Ask for user input and validate the input
# 2. Update the board
# 3. Check win or tie situation
# 4. Switch User
while not gameEnded:
    move = input(currentTurnPlayer + "'s turn, input: ")

    while not validateMove(move):
        print("Oops..invalid input. Please try again:")
        move = input(currentTurnPlayer + "'s turn, input: ")

    markBoard(move, currentTurnPlayer)

    printBoard()
    
    if checkWin(currentTurnPlayer):
        print ('Congratulations player: ' + currentTurnPlayer + ', You won the game.')
        restartGame()

    elif checkFull():
        print("It's a tie!")
        restartGame()

    else:
        if currentTurnPlayer == 'X':
            currentTurnPlayer = 'O'
        else:
            currentTurnPlayer = 'X'

        computer(board) 




        

        

    













    ##print (validateMove(move))
    #if validateMove(move) == True:
    #    markBoard(move, currentTurnPlayer)
     #   printBoard()
        
       # if checkWin(currentTurnPlayer) == True:
       #     print ('Congratulations player: ' + currentTurnPlayer + ', You won the game.')
        #    print('Would you like to restart the game? Y/N')
        #    restart = input()
        #    if restart == 'Y':
        #        board = board.fromkeys(board, ' ')
        #       gameEnded = False
        #    elif restart == 'N':
         #       gameEnded = True
        #else:
           # if checkFull() == False:
            #    if currentTurnPlayer == 'X':
            #        currentTurnPlayer = 'O'
             #   else:
             #       currentTurnPlayer = 'X'
            #else:
             #   print ("It's a tie! Would you like to restart the game? Y/N")
            #    restart = input()
             #   if restart == 'Y':
             #       board = board.fromkeys(board, ' ')
             #       gameEnded = False
              #  elif restart == 'N':
              #      gameEnded = True

            
#else:
   # move = input("Sorry, please try a different number, input: ")
            










# Bonus Point: Implement the feature for the user to restart the game after a tie or game over
