print("welcome to favour's TIC TAC TOE game")

board = ['index one not in use ',' ',' ',' ',' ',' ',' ',' ',' ',' '] 

# TO display the board and its index value
def board_display(board):
    
    
    print(board[1],"|",board[2],"|",board[3])
    print(board[4],"|",board[5],"|",board[6])
    print(board[7],"|",board[8],"|",board[9])
    return " "
print("this is our unupdated board")

print(board_display(board))# input collector function

# Ask player one to chose X or O

inputVal = " "
    
while inputVal != "X" and inputVal != "O":
        
    inputVal_ = input("Player 1, Chose between \'X\' or \'O\':  ")
    inputVal_ = inputVal_.upper()
            
    if inputVal_ == "X":
        player_1 = inputVal_
        player_2 = "O"
    inputVal = inputVal_
               
    if inputVal_ == "O":
        player_1 = inputVal_
        player_2 = "X"
    inputVal = inputVal_
        
        
count = 1
while count < 10:
    
    print("Player_1, which position do you wanna play in")
    rep_position = range(1,10)
    
    pos = 0
     
    while pos not in (range(1,10)):
        try:
            pos = int(input("Enter position to play from (1-9): "))
            #checks if there is space
            if board[pos] == " ": 
                print("position ",pos," is empty")

                board[pos] = player_1

                print("Updated board")

                print(board_display(board))


            else:
                print("position ",pos," is field")
                
                while board[pos] != " ":
                    print("Enter another position again")
                    pos = int(input("Enter another position to play from (1-9): "))
                else:
                    print("position ",pos," is empty")

                    board[pos] = player_1

                    print("Updated board")

                    print(board_display(board))
                    
                    # handling words entered
        except:
            print("Invalid input")
                


        # check if any line is the same,equal or different

    if ((board[1]==board[2]==board[3]==player_1)or
            (board[4]==board[5]==board[6]==player_1)or
            (board[7]==board[8]==board[9]==player_1)or
            (board[1]==board[4]==board[7]==player_1)or
            (board[2]==board[5]==board[8]==player_1)or
            (board[3]==board[6]==board[9]==player_1)or
            (board[1]==board[5]==board[9]==player_1)or
            (board[3]==board[5]==board[7]==player_1)) == True:
        print("player_1 wins")
        break
    else:
        pass

    # checking if board is field
    
    if (board[1]== " ")or(board[2]== " ")or(board[3]== " ")or(board[4]== " ")or(board[5]== " ")or(board[6]== " ")or(board[7]== " ")or(board[8]== " ")or(board[9]== " "):
        print("Board is not full")
        
        print("Player_2, which position do you wanna play in")
        rep_position = range(1,10)

        pos = 0

        while pos not in (range(1,10)):
            try:
                pos = int(input("Enter position to play from (1-9): "))
                #checks if there is space
                if board[pos] == " ": 
                    print("position ",pos," is empty")

                    board[pos] = player_2

                    print("Updated board")

                    print(board_display(board))


                else:
                    print("position ",pos," is field")

                    while board[pos] != " ":
                        print("Enter another position again")
                        pos = int(input("Enter another position to play from (1-9): "))
                    else:
                        print("position ",pos," is empty")

                        board[pos] = player_2

                        print("Updated board")

                        print(board_display(board))

                # handling words entered
            except:
                print("Invalid input")
                
        if ((board[1]==board[2]==board[3]==player_1)or
                (board[4]==board[5]==board[6]==player_2)or
                (board[7]==board[8]==board[9]==player_2)or
                (board[1]==board[4]==board[7]==player_2)or
                (board[2]==board[5]==board[8]==player_2)or
                (board[3]==board[6]==board[9]==player_2)or
                (board[1]==board[5]==board[9]==player_2)or
                (board[3]==board[5]==board[7]==player_2)) == True:
            print("player_2 wins")
            break
        else:
            pass
        
    elif  (board[1]!= " ")and(board[2]!= " ")and(board[3]!= " ")and(board[4]!= " ")and(board[5]!= " ")and(board[6]!= " ")and(board[7]!= " ")and(board[8]!= " ")and(board[9]!= " "):
        print("Board is full")
        
        print("\n")
        
        print("Its a tie")
        
        respond = "" 
        
        while respond != "YES" and respond != "NO":
            respond = input("Still wanna play? (yes/no)  :").upper()
        
        if respond == "YES":
            
            while respond == "YES":
            
                print("welcome to fav TIC TAC TOE game")

                board = ['index one not in use ',' ',' ',' ',' ',' ',' ',' ',' ',' '] 


                # TO display the board and its index value
                def board_display(board):
                  

                    print(board[1],"|",board[2],"|",board[3])
                    print(board[4],"|",board[5],"|",board[6])
                    print(board[7],"|",board[8],"|",board[9])
                    return " "
                print("This is our unupdated board")

                print(board_display(board))# input collector function

                # Ask player one to chose X or O

                inputVal = " "

                while inputVal != "X" and inputVal != "O":

                    inputVal_ = input("Player 1, Chose between \'X\' or \'O\':  ")
                    inputVal_ = inputVal_.upper()

                    if inputVal_ == "X":
                        player_1 = inputVal_
                        player_2 = "O"
                    inputVal = inputVal_

                    if inputVal_ == "O":
                        player_1 = inputVal_
                        player_2 = "X"
                    inputVal = inputVal_


                count = 1
                while count < 10:

                    print("Player_1, which position do you wanna play in")
                    rep_position = range(1,10)

                    pos = 0

                    while pos not in (range(1,10)):
                        try:
                            pos = int(input("Enter position to play from (1-9): "))
                            #checks if there is space
                            if board[pos] == " ": 
                                print("position ",pos," is empty")

                                board[pos] = player_1

                                print("Updated board")

                                print(board_display(board))


                            else:
                                print("position ",pos," is field")

                                while board[pos] != " ":
                                    print("Enter another position again")
                                    pos = int(input("Enter another position to play from (1-9): "))
                                else:
                                    print("position ",pos," is empty")

                                    board[pos] = player_1

                                    print("Updated board")

                                    print(board_display(board))

                                    # handling words entered
                        except:
                            print("Invalid input")



                        # check if any line is the same,equal or different

                    if ((board[1]==board[2]==board[3]==player_1)or
                            (board[4]==board[5]==board[6]==player_1)or
                            (board[7]==board[8]==board[9]==player_1)or
                            (board[1]==board[4]==board[7]==player_1)or
                            (board[2]==board[5]==board[8]==player_1)or
                            (board[3]==board[6]==board[9]==player_1)or
                            (board[1]==board[5]==board[9]==player_1)or
                            (board[3]==board[5]==board[7]==player_1)) == True:
                        print("player_1 wins")
                        break
                    else:
                        pass

                    # checking if board is field

                    if (board[1]== " ")or(board[2]== " ")or(board[3]== " ")or(board[4]== " ")or(board[5]== " ")or(board[6]== " ")or(board[7]== " ")or(board[8]== " ")or(board[9]== " "):
                        print("Board is not full")

                        print("Player_2, which position do you wanna play in")
                        rep_position = range(1,10)

                        pos = 0

                        while pos not in (range(1,10)):
                            try:
                                pos = int(input("Enter position to play from (1-9): "))
                                #checks if there is space
                                if board[pos] == " ": 
                                    print("position ",pos," is empty")

                                    board[pos] = player_2

                                    print("Updated board")

                                    print(board_display(board))


                                else:
                                    print("position ",pos," is field")

                                    while board[pos] != " ":
                                        print("Enter another position again")
                                        pos = int(input("Enter another position to play from (1-9): "))
                                    else:
                                        print("position ",pos," is empty")

                                        board[pos] = player_2

                                        print("Updated board")

                                        print(board_display(board))

                                # handling words entered
                            except:
                                print("Invalid input")
                                
                        if ((board[1]==board[2]==board[3]==player_1)or
                                (board[4]==board[5]==board[6]==player_2)or
                                (board[7]==board[8]==board[9]==player_2)or
                                (board[1]==board[4]==board[7]==player_2)or
                                (board[2]==board[5]==board[8]==player_2)or
                                (board[3]==board[6]==board[9]==player_2)or
                                (board[1]==board[5]==board[9]==player_2)or
                                (board[3]==board[5]==board[7]==player_2)) == True:
                            print("player_2 wins")
                            break
                        else:
                            pass
                                
                                
                    elif (board[1]!= " ")and(board[2]!= " ")and(board[3]!= " ")and(board[4]!= " ")and(board[5]!= " ")and(board[6]!= " ")and(board[7]!= " ")and(board[8]!= " ")and(board[9]!= " "):
                        print("Board is full")

                        print("\n")

                        print("Its a tie")

                        respond = "" 

                        while respond != "YES" and respond != "NO":
                            respond = input("Still wanna play? (yes/no)  :").upper()

                        if respond == "YES":    
                            
                            while respond == "YES":
            
                                print("welcome to fav TIC TAC TOE game")

                                board = ['index one not in use ',' ',' ',' ',' ',' ',' ',' ',' ',' '] 

                                
                                # TO display the board and its index value
                                def board_display(board):
                                    

                                    print(board[1],"|",board[2],"|",board[3])
                                    print(board[4],"|",board[5],"|",board[6])
                                    print(board[7],"|",board[8],"|",board[9])
                                    return " "
                                print("This is our unupdated board")

                                print(board_display(board))# input collector function

                                # Ask player one to chose X or O

                                inputVal = " "

                                while inputVal != "X" and inputVal != "O":

                                    inputVal_ = input("Player 1, Chose between \'X\' or \'O\':  ")
                                    inputVal_ = inputVal_.upper()

                                    if inputVal_ == "X":
                                        player_1 = inputVal_
                                        player_2 = "O"
                                    inputVal = inputVal_

                                    if inputVal_ == "O":
                                        player_1 = inputVal_
                                        player_2 = "X"
                                    inputVal = inputVal_


                                count = 1
                                while count < 10:

                                    print("Player_1, which position do you wanna play in")
                                    rep_position = range(1,10)

                                    pos = 0

                                    while pos not in (range(1,10)):
                                        try:
                                            pos = int(input("Enter position to play from (1-9): "))
                                            #checks if there is space
                                            if board[pos] == " ": 
                                                print("position ",pos," is empty")

                                                board[pos] = player_1

                                                print("Updated board")

                                                print(board_display(board))


                                            else:
                                                print("position ",pos," is field")

                                                while board[pos] != " ":
                                                    print("Enter another position again")
                                                    pos = int(input("Enter another position to play from (1-9): "))
                                                else:
                                                    print("position ",pos," is empty")

                                                    board[pos] = player_1

                                                    print("Updated board")

                                                    print(board_display(board))

                                                    # handling words entered
                                        except:
                                            print("Invalid input")



                                        # check if any line is the same,equal or different

                                    if ((board[1]==board[2]==board[3]==player_1)or
                                            (board[4]==board[5]==board[6]==player_1)or
                                            (board[7]==board[8]==board[9]==player_1)or
                                            (board[1]==board[4]==board[7]==player_1)or
                                            (board[2]==board[5]==board[8]==player_1)or
                                            (board[3]==board[6]==board[9]==player_1)or
                                            (board[1]==board[5]==board[9]==player_1)or
                                            (board[3]==board[5]==board[7]==player_1)) == True:
                                        print("player_1 wins")
                                        break
                                    else:
                                        pass

                                    # checking if board is field

                                    if (board[1]== " ")or(board[2]== " ")or(board[3]== " ")or(board[4]== " ")or(board[5]== " ")or(board[6]== " ")or(board[7]== " ")or(board[8]== " ")or(board[9]== " "):
                                        print("Board is not full")

                                        print("Player_2, which position do you wanna play in")
                                        rep_position = range(1,10)

                                        pos = 0

                                        while pos not in (range(1,10)):
                                            try:
                                                pos = int(input("Enter position to play from (1-9): "))
                                                #checks if there is space
                                                if board[pos] == " ": 
                                                    print("position ",pos," is empty")

                                                    board[pos] = player_2

                                                    print("Updated board")

                                                    print(board_display(board))


                                                else:
                                                    print("position ",pos," is field")

                                                    while board[pos] != " ":
                                                        print("Enter another position again")
                                                        pos = int(input("Enter another position to play from (1-9): "))
                                                    else:
                                                        print("position ",pos," is empty")

                                                        board[pos] = player_2

                                                        print("Updated board")

                                                        print(board_display(board))

                                                # handling words entered
                                            except:
                                                print("Invalid input")

                                        if ((board[1]==board[2]==board[3]==player_1)or
                                                (board[4]==board[5]==board[6]==player_2)or
                                                (board[7]==board[8]==board[9]==player_2)or
                                                (board[1]==board[4]==board[7]==player_2)or
                                                (board[2]==board[5]==board[8]==player_2)or
                                                (board[3]==board[6]==board[9]==player_2)or
                                                (board[1]==board[5]==board[9]==player_2)or
                                                (board[3]==board[5]==board[7]==player_2)) == True:
                                            print("player_2 wins")
                                            break
                                        else:
                                            pass
                                        
                                    elif (board[1]!= " ")and(board[2]!= " ")and(board[3]!= " ")and(board[4]!= " ")and(board[5]!= " ")and(board[6]!= " ")and(board[7]!= " ")and(board[8]!= " ")and(board[9]!= " "):
                                        print("Board is full")

                                        print("\n")

                                        print("Its a tie")
                                        break
                                    break  
                                break
                        elif respond == "NO":
                            break

                respond = input("Ohhh!!! still wanna play? (yes/no)  :").upper()

            break
            
        elif respond == "NO":
            break

    count = count + 2
    