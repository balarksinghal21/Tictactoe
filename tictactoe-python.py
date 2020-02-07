pos = [" " for i in range(10)]
pos[5] = "O"

def inslet(lett,posi):
    pos[posi] = lett

def spacefree(posi):
    return pos[posi] == " "

def print_board():#to display values on board
    print(" ",pos[1]," | ",pos[2]," | ",pos[3])
    print("-----|-----|-----")
    print(" ",pos[4]," | ",pos[5]," | ",pos[6])
    print("-----|-----|-----")
    print(" ",pos[7]," | ",pos[8]," | ",pos[9])

def comp_select():
    possiblemoves = [x for x,letter in enumerate(pos) if letter ==" " and x != 0]
    move = 0

    for let in ["X"]:
        for i in possiblemoves:
            bcopy = pos[:]
            bcopy[i] = let
            if (is_win(bcopy,let)):
                move = i
                return move
    cornersopen =[]
    for i in possiblemoves:
        if i in [1,3,7,9]:
            cornersopen.append(i)
    if len(cornersopen)>0:
        move = selectrandom(cornersopen)
        bcopy[move] ="O"
        if not(is_win(bcopy,"O")):
            return move
        else:
            cornersopen.remove(move)
            move = selectrandom(cornersopen)
            return move
    edgesopen =[]
    for i in possiblemoves:
        if i in [2,4,6,8]:
            edgesopen.append(i)
    if len(edgesopen)>0:
        move = selectrandom(edgesopen)
        if not(is_win(bcopy,"O")):
            return move
        else:
            edgesopen.remove(move)
            move = selectrandom(edgesopen)
            return move
    if(move == 0 and len(possiblemoves)==0):
        return move
    else:
        move = selectrandom(possiblemoves)
        return move

def selectrandom(lis):
    import random
    ln =len(lis)
    if(len(lis)>0):
        r = random.randrange(0,ln)
        return  lis[r]
    else:
        return 0

def is_win(bo,le):
    return (bo[1] == le and bo[2] == le and bo[3] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (bo[3] == le and bo[6] == le and bo[9] == le) or (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (bo[2] == le and bo[5] == le and bo[8] == le) or (bo[1] == le and bo[5] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo[7] == le)
    
def usr_ent():
    run =True
    while run:
        ent = input("Please enter a Position to insert a 'X'(1-9): ")
        try:
            ent = int(ent)    
            if(ent>0 and ent<10):
                if(spacefree(ent)):
                    run = False
                    inslet("X",ent)
                else:
                    print("Sorry, Space Is Already Occupied!")
            else:
                print("Please Enter A Choice Within Range!")
        except:
            print("Please Type A Number!")

def isBoardfull(board):
    if pos.count(" ") > 1 :
        return False
    else:
        return True

def main():
    print("Welcome To Tic-Tac-Toe  Game!!!\n")
    print("Rules Are As Follows: \n1). You Are Playing As a 'X'\n2). There is Already a 'O' Present in the middle\n3). First One to get a 3 in row WINS.\n\n")
    print_board()
    while not(isBoardfull(pos)):
        if not(is_win(pos,"O")):
            usr_ent()
            print_board()
        else:
            print("Sorry!,O\'s won This Time")
            break
        if not(is_win(pos,"X")):
            move = comp_select()
            if(move == 0):
                print("Tie Game!")
            else:
                inslet("O",move)
                print("Computer Inserted An 'O' in Position :",move)
                print_board()
        else:
            print("Congratulations! X\'s Won this Time. Good Job!")
            break
    if isBoardfull(pos):
        print("Tie Game")
    
main()
