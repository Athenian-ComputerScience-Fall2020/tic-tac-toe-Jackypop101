# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  https://medium.com/byte-tales/the-classic-tic-tac-toe-game-in-python-3-1427c68b8874 I used this website not to directly copy and paste everything down but to take ideas from it and creating my own version of the game. For the first part it is similar because I can not think of a better way to word the functions. 

# A note on style: Dictionaries can be defined before or after functions.


#Defining the Board with keys as TL, TM, TR, ML, MM, MR, BL, BM, BR. T means top, M means mid, B means bot, L means left, R means right. And the values of the keys are blank and will be added on to with either X or O later on. 
theboard = {'TL': ' ' , 'TM': ' ' , 'TR': ' ' ,
            'ML': ' ' , 'MM': ' ' , 'MR': ' ' ,
            'BL': ' ' , 'BM': ' ' , 'BR': ' ' }

#Board printing function, prints out the value of each key which makes it easier to plug a place(for ex. TL) in and put down either X or O later on in the game function. 
#'|' and '-+-+-' are from the readme instructions

def printboard(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])

#Game fuction, ttt for "Tick Tack Toe"
def ttt():
    turn = 'X'
    num = 0
#for loop to ask the player for input 9 times.
    while num < 10:
        printboard(theboard)
        print("It's your turn " + turn + ". Where do you want to place?")
        try:
            move = input()        
#if the place on the board does not have anything already on it, it can be ocupied by turn, which is either X or O.
# #Adding 1 to the count because the total can only be 9 because there are only 9 spaces. 
            if theboard[move] == ' ':
                theboard[move] = turn
                num += 1
                if turn == "X":
                    turn = "O"
                elif turn == "O":
                    turn = "X"
#If there is already something on that space the system is going to tell the user to move it's piece elsewhere. 
            elif theboard[move] != ' ':
                print("Space is taken, move elsewhere.")
                if turn == "X":
                    turn = "O"
                elif turn == "O":
                    turn = "X"
                continue
#Cheking system: To check every row and colum and diagonal rows to see if all three are the same. Either X or O.
            if num < 9:
                #left column
                if theboard['BL'] == theboard['ML'] == theboard['TL'] == 'X':
                    printboard(theboard)
                    print("X" + " Won!!!")
                    break
                elif theboard['BL'] == theboard['ML'] == theboard['TL'] == 'O':
                    printboard(theboard)
                    print("O" + " Won!!!")
                    break
                #middle column
                elif theboard['BM'] == theboard['MM'] == theboard['TM'] == 'X':
                    printboard(theboard)
                    print("X" + " Won!!!")
                    break
                elif theboard['BM'] == theboard['MM'] == theboard['TM'] == 'O':
                    printboard(theboard)
                    print("O" + " Won!!!")
                    break
                #right colume
                elif theboard['BR'] == theboard['MR'] == theboard['TR'] == 'X':
                    printboard(theboard)
                    print("X" + " Won!!!")
                    break
                elif theboard['BR'] == theboard['MR'] == theboard['TR'] == 'O':
                    printboard(theboard)
                    print("O" + " Won!!!")
                    break
                #top row
                elif theboard['TL'] == theboard['TM'] == theboard['TR'] == 'X':
                    printboard(theboard)
                    print("X" + " Won!!!")
                    break
                elif theboard['TL'] == theboard['TM'] == theboard['TR'] == 'O':
                    printboard(theboard)
                    print("O" + " Won!!!")
                    break
                #mid row
                elif theboard['ML'] == theboard['MM'] == theboard['MR'] == 'X':
                    printboard(theboard)
                    print("X" + " Won!!!")
                    break
                elif theboard['ML'] == theboard['MM'] == theboard['MR'] == 'O':
                    printboard(theboard)
                    print("O" + " Won!!!")
                    break
                #bot row
                elif theboard['BL'] == theboard['BM'] == theboard['BR'] == 'X':
                    printboard(theboard)
                    print("X" + " Won!!!")
                    break
                elif theboard['BL'] == theboard['BM'] == theboard['BR'] == 'O':
                    printboard(theboard)
                    print("O" + " Won!!!")
                    break
                #left diagonal 
                elif theboard['TL'] == theboard['MM'] == theboard['BR'] == 'X':
                    printboard(theboard)
                    print("X" + " Won!!!")
                    break
                elif theboard['TL'] == theboard['MM'] == theboard['BR'] == 'O':
                    printboard(theboard)
                    print("O" + " Won!!!")
                    break
                #right diagonal
                elif theboard['BL'] == theboard['MM'] == theboard['TR'] == 'X':
                    printboard(theboard)
                    print("X" + " Won!!!")
                    break
                elif theboard['BL'] == theboard['MM'] == theboard['TR'] == 'O':
                    printboard(theboard)
                    print("O" + " Won!!!")
                    break
            # If no one won after 9 round which means that the whole board is filled, then the game would be a tie.
            if num == 9:
                printboard(theboard)
                print("Tie Game!!!")
                break
        #Giving the player a chance to redo their input if they entered a wrong input.
        except:
            print("You made a mistake please us inputs, TL, TM, TR, ML, MM, MR, BL, BM, BR") 
            continue
            
print("Hello players, this is a simple and fun game called:")
print("TICK!")
print("TAC!")
print('TOE!')
print("*****")
print("This is a 2 player game, the starting player is X and the second player is O. Both players will take turns marking the spaces in a 3×3 grid. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row first is the winner. By the end of 9 rounds meaning that if all the squares are full, it is a tie.")
print("Good luck players and let the game begin!")

#running game
ttt()

#Asking the players if they whould like to play or quit again after they either won or tied.
while True:
    a = input('Would you like to restart? Enter Y to play, Enter N to quit.')
    if a == "Y":
        theboard['TL'] = ' '
        theboard['ML'] = ' '
        theboard['BL'] = ' '
        theboard['TM'] = ' '
        theboard['MM'] = ' '
        theboard['BM'] = ' '
        theboard['TR'] = ' '
        theboard['MR'] = ' '
        theboard['BR'] = ' '
        ttt()

    if a == "N":
        print("Hope you can play again soon!")



