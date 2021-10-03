def isSafe(row, col, val, board):
    for i in range(0,9):
        if (board[i][col] == val):
            return False
        if (board[row][i] == val):
            return False
        if (board[3*(row//3) + i//3][3*(col//3) + i%3] == val):
            return False
    return True

def solve(board):
    for i in range(0,9):
        for j in range(0,9):
            
            if (board[i][j] == 0):       
                
                for val in range(1,10):
                    
                    if (isSafe(i, j, val, board)):
                        board[i][j] = val
                        
                        if (solve(board)):
                            return True
                        
                        board[i][j] = 0  
                
                return False
    
    return True


if __name__ == "__main__":
    board = [[3 ,0, 0, 8, 0, 1, 0, 0, 2],
            [2, 0, 1, 0, 3, 0, 6, 0, 4],
            [0, 0, 0, 2, 0, 4, 0, 0, 0],
            [8, 0, 9, 0, 0, 0, 1, 0, 6],
            [0, 6, 0, 0, 0, 0, 0, 5, 0],
            [7, 0, 2, 0, 0, 0, 4, 0, 9],
            [0, 0, 0, 5, 0, 9, 0, 0, 0],
            [9, 0, 4, 0, 8, 0, 7, 0, 5],
            [6, 0, 0, 1, 0, 7, 0, 0, 3]]
    
    def printBoard():
        for i in range(0,9):
            for j in range(0,9):
                print(board[i][j],end = " ")
            print()
    
    solve(board)
    print('Sudoku Board : \n')
    printBoard()
