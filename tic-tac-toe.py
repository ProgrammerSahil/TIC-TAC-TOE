
board = [

    ".", ".", ".",
    
    ".", ".", ".",

    ".", ".", "."

    ]
chars = ["X", "O"]

class game:
    def __init__(self, board):
        self.board = board
        

    def fill(self, idx, symbol):
        try:
            if idx<=-1:
                print("")
                print("The provided position is out of range!")
                print("Your turn wil be skipped!")
                print("")
            else:
                if self.board[idx] in chars:
                    print("")
                    print("Spot already taken")
                    print("Your turn will be skipped")
                    print("")
                else:
                    self.board[idx] = symbol
        except IndexError:
            print("")
            print("The provided position is out of range!")
            print("Your turn will be skipped!")
            print("")
        except ValueError:
            print("")
            print("Enter a valid position!")
            print("Your turn will be skipped!")
            print("")
    def display(self):
        j = len(self.board)
        i=0
        while(i < j):
            if(i==0 or i == 3 or i == 6):
                print("|", self.board[i],"|", end="")
            elif(i==1 or i==4 or i==7):
                print(self.board[i],"|", end="")
            else:
                print(self.board[i], "|")
                print("")
            i+=1

    # the following method will develop the logic for the tic-tac-toe game

    def check(self):
        if(self.board[0] == self.board[1] and self.board[1] == self.board[2] and self.board[0] in chars ):
            winIdx = chars.index(self.board[0])
            return chars[winIdx]
        elif(self.board[0] == self.board[3] and self.board[3] == self.board[6] and self.board[0] in chars):
            winIdx = chars.index(self.board[0])
            return chars[winIdx]
        elif(self.board[0] == self.board[4] and self.board[4] == self.board[8] and self.board[0] in chars):
            winIdx = chars.index(self.board[0])
            return chars[winIdx]
        elif(self.board[1] == self.board[4] == self.board[7] and self.board[1] in chars):
            winIdx = chars.index(self.board[1])
            return chars[winIdx]
        elif(self.board[2] == self.board[4] == self.board[6] and self.board[2] in chars):
            winIdx = chars.index(self.board[2])
            return chars[winIdx]
        elif(self.board[2] == self.board[5] == self.board[8] and self.board[2] in chars):
            winIdx = chars.index(self.board[2])
            return chars[winIdx]
        elif(self.board[3] == self.board[4] == self.board[5] and self.board[3] in chars):
            winIdx = chars.index(self.board[3])
            return chars[winIdx]
        else:
            pass


new = game(board)
new.display()
Curr = "O"
while True:
    stat = "Enter the place (1-9) for "+Curr+" : "
    index = int(input(stat))
    new.fill(index-1, Curr)
    new.display()
    winner = new.check()

    if winner != None:
        print(winner+" Won")
        break

    if Curr == "O":
        Curr = "X"
    else:
        Curr = "O"

print("")
print("Thanks for playing")
input("Press <Enter> to exit the game")
print("")
    

        
