mainlist = [["1", "2", "3"],["4", "5", "6"],["7", "8", "9"]]
def grid():
    print("\n --|---|-- \n".join([" "+" | ".join(sublist) for sublist in mainlist]))
grid()
def checktype(list):
    for element in list:
        if isinstance(element, str):
            break
        else:
            print("Game Over.")
        
def round(turn):
      
        symbols = ["X", "O"]
        symbol = symbols[turn % 2]
        input_valid = False
        while(not input_valid):
            choice = input("Choose your cell : ")
            idx = (int(choice)-1) % 3
            idy = (int(choice)-1) // 3
            value = mainlist[idy][idx]
            if value == "X" or value == "O":
                print("Please choose an available cell.")
            else:    
                mainlist[idy][idx] = symbol
                input_valid = True
        grid()
        return idx, idy, symbols, symbol
    
for tour in range(9):
    idx, idy, symbols, symbol = round(tour)
    diago = [mainlist[di][di] for di in range(3)]
    diagoo = [mainlist[dia][abs(2 - dia)] for dia in range(3)]
    checkerv = [mainlist[i][idx] == symbol for i in range(3)]
    checkerh = [mainlist[idy][j] == symbol for j in range(3)]
    checkerd = [diago[d1] == symbol for d1 in range(3)]
    checkerdd = [diagoo[d2] == symbol for d2 in range(3)]

    if checkerv == [True for rowidv in range(3)] or checkerh == [True for rowidh in range(3)] or checkerd == [True for rowidd in range(3)] or checkerdd == [True for rowiddd in range(3)]:   
        print("Game over, " + symbol + " wins!")
        break
    elif tour == 8:
        print("Game over, it's a draw.")
        break
    else:
        continue
