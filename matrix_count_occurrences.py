def count_occurrences(matrix1, int1):
    count = 0
    for element in matrix1:
        print(element)
    print(int1)
    for value in matrix1:
            if value == int1:
                count += 1
    return count
def main():
    matrix1 = [7]
    int1 = 4
    result = count_occurrences(matrix1, int1)
    print(result)
main()