import random

#Function to display header
def header():
    for x in range(52):
        print("=", end='')
    print()
    print('''\t\t   TIC-TAC-TOE
\t\tHUMAN VS COMPUTER''')
    for i in range(0,52,1):
        print("=", end='')
    print()

def display_board(b,p,pc):
    print('   C1  C2  C3')
    for r in range(0,len(b),1):
        print("R" + str(r + 1) + ' ',end = '')
        for c in range(0,len(b[r]),1):
            print(b[r][c],end = '')
            if c < 2:
                print(" | ",end = '')
        print('\n',end = '')
    print("HUMAN = " + p + "\tCOMPUTER = " + pc)

#Function to display instructions
def instructions():
    header()
    print("Choose the symbol you want to play with first, 'X' or 'O'.")
    print("In this example, the symbol choosen is 'X'.")
    p = 'X'
    pc = 'O'
    b = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    display_board(b,p,pc)
    print("Enter the row and column for the position you want to place the symbol when asked.")
    print("Please choose the row where the '" + p + "' should be placed: 2")
    print("Please choose the column where the '" + p + "' should be placed: 2")
    print("After choosing, the game will display where you placed the symbol.")
    b = [[' ',' ',' '],[' ','X',' '],[' ',' ',' ']]
    header()
    display_board(b,p,pc)
    print("The computer will then move and display the position of the '" + pc + "' placed.")
    b = [[' ',' ',' '],[' ','X',' '],[' ',' ','O']]
    header()
    display_board(b,p,pc)
    print("The computer placed a '" + pc + "' on row 3, column 3")
    print("Continue and place 3 of your symbol in a horizontal, vertical, and diagonal row to win the game.")
    print("You lose the game if the computer achieve the win condition faster before you.")
    print("The game ends in a tie if there is no winner after filling the board.")    

#Function to check if the postion is occupied    
def check_occupied(b,r,c):
    if b[r - 1][c - 1] != ' ':
        return True

#Function to ask player to input position for symbol to be placed
def player_move(b,s):
    repeat = 1
    while repeat == 1:
        r = 0
        c = 0
        while True:
            try:
                #Ask player to choose the piece position
                while r < 1 or r > 3:
                    r = int(input("Please choose the row where the '" + s + "' should be placed: "))
                    if r < 1 or r > 3:
                        print("Error! Please enter a value that is between 1 to 3.")
                while c < 1 or c > 3:
                    c = int(input("Please choose the column where the '" + s + "' should be placed: "))
                    if c < 1 or c > 3:
                        print("Error! Please enter a value that is between 1 to 3.")
                break
            except ValueError:
                print("Error! Please enter an integer.")
        if check_occupied(b,r,c): #check if the position is occupied
            print("That position is occupied. Please choose a different position.")
        else:
            b[r - 1][c - 1] = s
            repeat = 0
    move = [b,r,c]
    return move

#Function to choose position randomly in a list for the computer to move
def computer_move(b,s):
    while True:
        r = random.randint(0,len(b)-1)
        c = random.randint(0,len(b[r])-1)
        if not check_occupied(b,r+1,c+1): #check if the position is occupied
            b[r][c] = s
            break
    move = [b,r + 1,c + 1]
    return move

#Function to check if the player or computer fulfill the win condition
def check_win(b,s):
    status = "CONTINUE"
    for r in range(0,len(b),1):
        count = 0
        for c in range(0,len(b[r]),1):
            if b[r][c] == s:
                count = count + 1
            if count == 3:
                status = "WIN"
                return status

    r = 0
    c = 0
    for c in range(0,len(b[r]),1):
        count = 0
        for r in range(0,len(b),1):
            if b[r][c] == s:
                count = count + 1
            if count == 3:
                status = "WIN"
                return status
            
    if ((b[0][2] == s and b[1][1] == s and b[2][0] == s) or
        (b[0][0] == s and b[1][1] == s and b[2][2] == s)):
        status = "WIN"
        return status

    count = 0
    for r in range(0,len(b),1):
        for c in range(0,len(b[r]),1):
            if b[r][c] != ' ':
                count = count + 1
    if count == 9:
        status ="TIE"
        return status

    return status

#Funtion to run the main process flow of tic tac toe game
def game_process(b,p,pc):
    status = "CONTINUE"
    count = 0
    move_list = []
    f = open('logfile_22064505.txt','w')
    while status == "CONTINUE":
        header()
        display_board(b,p,pc)
        #Get the position chosen by the player
        move_list = player_move(b,p)
        b = move_list[0]
        row = move_list[1]
        column = move_list[2]
        status = check_win(b,p) #Check if the player reached the win condition
        count = count + 1
        f.write(str(count) + ', H, ' + str(row) + ', ' + str(column) + ', ' + p + '\n')
        if status == "WIN":
            header()
            display_board(b,p,pc)
            print("Congratulations!!! You have beaten the computer!!!")
        elif status == "TIE":
            header()
            display_board(b,p,pc)
            print("The game ended in a tie.")
        else:
            header()
            display_board(b,p,pc)
            header()
            #Get the position chosen by the computer
            move_list = computer_move(b,pc)
            display_board(b,p,pc)
            b = move_list[0]
            row = move_list[1]
            column = move_list[2]
            print("The computer placed a '" + pc + "' on row " + str(row) + ", column " + str(column))
            status = check_win(b,pc) #Check if the computer reached the win condition
            count = count + 1
            f.write(str(count) + ', C, ' + str(row) + ', ' + str(column) + ', ' + pc + '\n')
            if status == "WIN":
                print("You have lost to the computer. Try again next time.")
            elif status == "TIE":
                print("The game ended in a tie.")
    f.close()
    
again = 'Y'

#ask the user if they want to read the instruction
while again == 'Y':
    #display header
    header()
    while True:
        option = (input("Do you wish to read the instructions? (Y/N): ")).upper()
        if option == 'Y':
            #display the instructions
            instructions()
            break
        elif option == 'N':
            break
        else:
            print("Error! Please enter 'Y' or 'N'.")
    print("Enjoy the game!")
    board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    header()
    #ask the user to choose their symbol
    while True:
        player = (input("Please choose the symbol you wish to use ('X' or 'O'): ")).upper()
        if player == 'X':
            computer = 'O'
            break
        elif player == 'O':
            computer = 'X'
            break
        else:
            print("Error! Please choose the correct symbol ('X' or 'O')")

    #run the game process
    game_process(board,player,computer)

    #ask the user if they want to play again
    while True:
        again = (input("Do you wish to play again? (Y/N): ")).upper()
        if again == 'N':
            print("Thanks for playing!")
            break
        elif again == 'Y':
            break
        else:
            print("Wrong input, please enter 'Y' or 'N'.")
    
    
