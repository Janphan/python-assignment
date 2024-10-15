# Function to check if a row is ok
def row_ok(sudoku, row_index):
    seen_digits = []
    for num in sudoku[row_index]:
        if num != 0:
            if num in seen_digits:
                return False
            seen_digits.append(num)
    return True

# Function to check if a column is ok
def column_ok(sudoku, column_index):
    seen_digits = []
    for row in sudoku:
        num = row[column_index]
        if num != 0:
            if num in seen_digits:
                return False
            seen_digits.append(num)
    return True

# Function to check if a 3x3 block is ok
def block_ok(sudoku, row_index, column_index):
    valid_block_starts = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]
    if (row_index, column_index) not in valid_block_starts:
        return False
    
    seen_digits = []
    for i in range(row_index, row_index + 3):
        for j in range(column_index, column_index + 3):
            num = sudoku[i][j]
            if num != 0:
                if num in seen_digits:
                    return False
                seen_digits.append(num)
    
    return True

# Function to check if the entire grid is ok
def grid_ok(sudoku):
    # Check each row
    for row_index in range(9):
        if not row_ok(sudoku, row_index):
            return False
    
    # Check each column
    for column_index in range(9):
        if not column_ok(sudoku, column_index):
            return False
    
    # Check each 3x3 block
    for row_index, column_index in [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]:
        if not block_ok(sudoku, row_index, column_index):
            return False
    
    return True

def main():
    sudoku_1 = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]
    
    sudoku_2 = [
        [2, 6, 7, 8, 3, 9, 5, 0, 4],
        [9, 0, 3, 5, 1, 0, 6, 0, 0],
        [0, 5, 1, 6, 0, 0, 8, 3, 9],
        [5, 1, 9, 0, 4, 6, 3, 2, 8],
        [8, 0, 2, 1, 0, 5, 7, 0, 6],
        [6, 7, 4, 3, 2, 0, 0, 0, 5],
        [0, 0, 0, 4, 5, 7, 2, 6, 3],
        [3, 2, 0, 0, 8, 0, 0, 5, 7],
        [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]
    
    print(grid_ok(sudoku_1))  # False
    print(grid_ok(sudoku_2))  # True

if __name__ == "__main__":
    main()
