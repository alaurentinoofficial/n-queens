def test_queen(row, col, queens):
    error = False

    for (row1, col1) in enumerate(queens):
        # Diagonal
        error = abs(row - row1) == abs(col - col1)
        # Vertical | Horizontal
        error = error or (row == row1 or col == col1)

        if error:
            break
    
    return not error

def n_queens(size=(8, 8), queens=[], row=0):
    rows_size, cols_size = size

    if rows_size == row:
        return queens
    
    max_lenght = []
    
    for col in range(cols_size):
        if test_queen(row, col, queens):
            queens.append(col)

            if len(queens) > len(max_lenght):
                max_lenght = queens

            forward = n_queens(size, queens[:], row+1)

            if len(forward) > len(max_lenght):
                max_lenght = forward

            queens = queens[:-1]
    
    return max_lenght
                

print(n_queens(size=(8,8)))