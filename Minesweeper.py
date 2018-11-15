
    #Minesweeper
import random
#-----------------------------------------------------------------#
    #define variables
board = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
n_mines = 0
x_mine = 0
y_mine = 0
alive = True
marked_spots = 0


#-----------------------------------------------------------------#
    #define Draw
def Draw(z):
    grid = ""
    for i in range(0,10):
        for j in range(0,10):
            if z[i][j] == 0 or z[i][j] == -1:
                grid = grid + "[ ]"
            elif z[i][j] > 0:
                grid = grid + " " + str(z[i][j]-10) +" "
            elif z[i][j] < -1:
                grid = grid + " " + "!" +" "
        grid = grid + "\n"
    print(grid)

#-----------------------------------------------------------------#
    #define Clear
def Clear(q,r,e):
    for l in range(r-1,r+2):
        for k in range(e-1,e+2):
            if l >= 0 and k >= 0 and l <= 9 and k <= 9:
                if q[l][k] == 0:
                    q[l][k] = 10
                    for y in range(l-1,l+2):
                        for x in range(k-1,k+2):
                            if y >= 0 and x >= 0 and y <= 9 and x <= 9:
                                if q[y][x] == -1 or q[y][x] == -3:
                                    q[l][k] = q[l][k] + 1
                    if q[l][k] == 10 and (l != r or k != e):
                        Clear(board , l , k)



    #define dificulty
#-----------------------------------------------------------------#
dificulty = int(input("Dificulty:\n-Easy(1)\n-Medium(2)\n-Hard(3)\n->"))

if dificulty == 1:
    n_mines = random.randint(13,17)
    for i in range(0 , n_mines):
        x_mine = random.randint(0,9)
        y_mine = random.randint(0,9)
        board[y_mine][x_mine] = -1
        


if dificulty == 2:
    n_mines = random.randint(26,34)
    for i in range(0 , n_mines):
        x_mine = random.randint(0,9)
        y_mine = random.randint(0,9)
        board[y_mine][x_mine] = -1
        

        
if dificulty == 3:
    n_mines = random.randint(45,55)
    for i in range(0 , n_mines):
        x_mine = random.randint(0,9)
        y_mine = random.randint(0,9)
        board[y_mine][x_mine] = -1

        
#-----------------------------------------------------------------#
        
    #draw board
print("[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]")


#-----------------------------------------------------------------#
    #def calculate n of mines
def mine_count(t,ide):
    n_mines = 0
    for i in range(0,10):
        n_mines = n_mines + t[i].count(ide)
    print("mines: ", n_mines)
    n = n_mines
    return n
#-----------------------------------------------------------------#
    #playing
origin_mines = 0
for i in range(0,10):
    origin_mines =  origin_mines + board[i].count(-1)
print("Mines:" , origin_mines)


while alive == True:
    choice = int(input("Open spot(1)\nMark mine (2)\nQuit (3)\n->"))

#-----------------------------------------------------------------#

    #testing guesses
    if choice == 1:
        guess_x = (int(input("x = ")) - 1)
        guess_y = (int(input("y = ")) - 1)

        if guess_x < 0 or guess_x > 9 or guess_y < 0 or guess_y > 9:
            print("Invalid")

        else:
            a = board[guess_y][guess_x]        
            if a == -1:
                alive = False
                print("Boom!")
    
                
            elif a == 0:
                board[guess_y][guess_x] = 10
                for y in range(guess_y-1,guess_y+2):
                    for x in range(guess_x-1,guess_x+2):
                        if y >= 0 and x >= 0 and y <= 9 and x <= 9:
                            if board[y][x] == -1 or board[y][x] == -3:
                                board[guess_y][guess_x] = board[guess_y][guess_x] + 1
                mine_count(board,-1)
                if board[guess_y][guess_x] == 10:
                    Clear(board , guess_y , guess_x)
                Draw(board)

            
            else:
                print("Invalid")
            
#-----------------------------------------------------------------#
            
    #Marking mines
    elif choice == 2:
        guess_x = (int(input("x = ")) - 1)
        guess_y = (int(input("y = ")) - 1)

        if guess_x < 0 or guess_x > 9 or guess_y < 0 or guess_y > 9:
            print("Invalid")

        else:
            if board[guess_y][guess_x] == 0 or board[guess_y][guess_x] == -1 and origin_mines > marked_spots:
                board[guess_y][guess_x] = board[guess_y][guess_x] - 2
                marked_spots += 1
                
            elif board[guess_y][guess_x] == -2 or board[guess_y][guess_x] == -3:
                board[guess_y][guess_x] = board[guess_y][guess_x] + 2
                marked_spots -= 1

            
        
        
        print("mines: ", origin_mines - marked_spots)
        Draw(board)

#-----------------------------------------------------------------#
        
    #Define victory condition
    elif origin_mines - mine_count(board,-2) == 0:
        alive = False
        print("Victory!")
        
#-----------------------------------------------------------------#
    if choice == 3:
        print("Are you sure you want to quit?(y to confirm)")
        end = input("")
        if end == 'y':
            alive = False
        else:
            continue
