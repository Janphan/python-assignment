def column_ok(sudoku, column_index):
    column = sudoku[column_index]
    seen_digits = []

    for row in sudoku:
        num = row[column_index]
        if num != 0:
            if num in seen_digits:
                return False
            else:
                seen_digits.append(num)
    return True
def main():
    sudoku = [
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
    print(column_ok(sudoku, column_index=0)) # False
    
    print(column_ok(sudoku, column_index=1)) # True
    print(column_ok(sudoku, column_index=8)) # True
if __name__ == "__main__":
    main()