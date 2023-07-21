
#prints board 2d char list in reverse order
def print_board(board):
    board.reverse()
    for x in board:
        print(' '.join(x))
    board.reverse()
    print()

#creates nested list for 2d chars, returns nested list
def initialize_board(num_rows,num_cols):
    board = []
    for i in range(0,num_rows):
        row = []
        for j in range(0,num_cols):
            row.append('-')
        board.append(row)
    return board

#compares col pos in each list until empty space is found, adds chip to board index
def insert_chip(board, col, chip_type):
    row = 0
    end = 0
    while end == 0:
        if chip_type == 'x':
                if board[row][col] == '-':
                    board[row][col] = 'x'
                    end = 1
                elif board[row][col] != '-':
                    row += 1

        elif chip_type == 'o':
            if board[row][col] == '-':
                board[row][col] = 'o'
                end = 1
            elif board[row][col] != '-':
                row += 1
    return row

#compares lists vertically and horizontally, if four in row returns winner
def check_if_winner(board,col,row,chip_type):
    rowString = ''
    rowList = []
    colList = []
    colString = ''
    win = False

    for item1 in board[row]:
        colList.append(item1)
   

    for item in board:
        for item2 in item[col]:
            rowList.append(item2)
  
    rowString = ' '.join(rowList)
    colString = ' '.join(colList)

    #checks for four in row
    if 'x x x x' in rowString or 'o o o o' in rowString:
        win = True
    if 'x x x x' in colString or 'o o o o' in colString:
        win = True
   
    return win

#checks if there are empty spaces left in board
def check_full(board):
    full = False
    x = [' '.join([str(c) for c in lst]) for lst in board]
    y = ' '.join(x)
    if '-' not in y:
        full = True        
    return full


def main():
    tie = False
    turn = 0
    win = False

    #creates board depending on user input
    board = initialize_board(int(input("What would you like the height of the board to be? ")), int(input("What would you like the length of the board to be? ")))
    print_board(board)
    print("Player 1: x")
    print("Player 2: o")
    print()

    #game ends when win or tie
    while win == False:
        
        if win == False:
            column = int(input("Player 1: Which column would you like to choose? "))
            row = insert_chip(board,column,'x')
            print_board(board)
            win = check_if_winner(board,column,row,'x')
            turn = 1
        

        if win == False:
            column = int(input("Player 2: Which column would you like to choose? "))
            row = insert_chip(board,column,'o')
            print_board(board)
            win = check_if_winner(board,column,row,'x')
            turn = 2

        if check_full(board) == True:
            print('Draw. Nobody wins.')
            break
    if win == True:
        print(f'Player {turn} won the game!')


if __name__ == "__main__":
    main()