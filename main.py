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

    # Check if gets in the maximum cases
    if rows_size == row:
        return queens
    
    # Save the max length
    max_lenght = []
    
    # Pass by each one column
    for col in range(cols_size):
        # Check if the actual position is valid
        if test_queen(row, col, queens):
            # Add the new queen
            queens.append(col)

            # Calls the next layer
            forward = n_queens(size, queens[:], row+1)

            # Check if the next layer results is grander than actual
            if len(forward) > len(max_lenght):
                max_lenght = forward

            # Remove this queen
            queens = queens[:-1]
    
    # Return the max length
    return max_lenght
                

print(n_queens(size=(8,8)))