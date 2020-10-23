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
            if num < 10:
                #left column
                if theboard['BL'] == theboard['ML'] == theboard['TL'] == 'X':
                    print("X" + " Won!!!")
                    break
                elif theboard['BL'] and theboard['ML'] and theboard['TL'] == 'O':
                    print("O" + " Won!!!")
                    break
                #middle column
                elif theboard['BM'] and theboard['MM'] and theboard['TM'] == 'X':
                    print("X" + " Won!!!")
                    break
                elif theboard['BM'] and theboard['MM'] and theboard['TM'] == 'O':
                #right column
                    print("O" + " Won!!!")
                    break
                elif theboard['BR'] and theboard['MR'] and theboard['TR'] == 'X':
                    print("X" + " Won!!!")
                    break
                elif theboard['BR'] and theboard['MR'] and theboard['TR'] == 'O':
                    print("O" + " Won!!!")
                    break
                #top row
                elif theboard['TL'] and theboard['TM'] and theboard['TR'] == 'X':
                    print("X" + " Won!!!")
                    break
                elif theboard['TL'] and theboard['TM'] and theboard['TR'] == 'O':
                    print("O" + " Won!!!")
                    break
                #mid row
                elif theboard['ML'] and theboard['MM'] and theboard['MR'] == 'X':
                    print("X" + " Won!!!")
                    break
                elif theboard['ML'] and theboard['MM'] and theboard['MR'] == 'O':
                    print("O" + " Won!!!")
                    break
                #bot row
                elif theboard['BL'] and theboard['BM'] and theboard['BR'] == 'X':
                    print("X" + " Won!!!")
                    break
                elif theboard['BL'] and theboard['BM'] and theboard['BR'] == 'O':
                    print("O" + " Won!!!")
                    break
                #left diagonal 
                elif theboard['TL'] and theboard['MM'] and theboard['BR'] == 'X':
                    print("X" + " Won!!!")
                    break
                elif theboard['TL'] and theboard['MM'] and theboard['BR'] == 'O':
                    print("O" + " Won!!!")
                    break
                #right diagonal
                elif theboard['BL'] and theboard['MM'] and theboard['TR'] == 'X':
                    print("X" + " Won!!!")
                    break
                elif theboard['BL'] and theboard['MM'] and theboard['TR'] == 'O':
                    print("O" + " Won!!!")
                    break
        except:
            print("You made a mistake please us inputs, TL, TM, TR, ML, MM, MR, BL, BM, BR") 
            continue

#running game
ttt()



