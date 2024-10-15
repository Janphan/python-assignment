def new_doubled_matrix(matrix):
    new_matrix = []
    for row in matrix:
        for element in row:
            new_row = element*2
            new_matrix.append(new_row)
    return new_matrix
def main():
 m1 = [[1, 2, 3], [4, 5, 6]]
 m2 = new_doubled_matrix(m1)
 print(m1)
 print(m2)
main()