# N-Queens

The ideal behind that problem it's how many queen it's possible put in a chessboard with the size NxM.

To test if a new queen is valid it's simple:

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