# N-Queens

The ideal behind that problem it's how many queen it's possible put in a chessboard with the size NxM.

**It's necessary create a validator for a new queen**

The queen just can move in dioganals, vertical and in horizontal, so...

1.  First check if has some queen in diagonal
    * `row` and `col` it's the pos of the new queen
    * `rowN` and `colN` it's the pos of anothers queens already placed 
```python
error = abs(row - rowN) == abs(col - colN)
```

2. Second is check if stay in Vertical and Horizontal
    * `row` and `col` it's the pos of the new queen
    * `rowN` and `colN` it's the pos of anothers queens already placed 
```python
error = (row == rowN or col == colN)
```

3. We need check for each one queen already placed
```python
def test_queen(row, col, queens):
    error = False

    for (rowN, colN) in enumerate(queens):
        # Diagonal
        error = abs(row - rowN) == abs(col - colN)
        # Vertical | Horizontal
        error = error or (row == rowN or col == colN)

        if error:
            break
    
    return not error
```


**After it's also need create a backtrack algorithm**
```python
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
```