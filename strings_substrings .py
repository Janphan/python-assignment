str1 = input("Enter a string: ")
char = input("Enter a character: ")
for i in range(len(str1) - 3):
    if str1[i] == char:
        print(str1[i:i+4])

