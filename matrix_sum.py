def print_matrix_sum(matrix1, matrix2):
    result = []
    for row in range(len(matrix1)):
        result_row = [] 
        for column in range (len(matrix1[0])):
            result_row.append(matrix1[row][column] + matrix2[row][column])
        result.append(result_row)
    
    for r in result:
       print(*r, end=" ")  # Print the row and end with a space
       print()
def main():
 m1 = [[1, 2, 0], [2, 3, 4]]
 m2 = [[3, 2, 5], [6, 4, 3]]
 m3 = [[1, 1, 1, 1], [3, 3, 2, 1], [2, 2, 2, 2]]
 m4 = [[2, 2, 2, 3], [2, 3, 1, 0], [1, 2, 3, 4]]
 print_matrix_sum(m1, m2)
 print()
 print_matrix_sum(m3, m4)
main()