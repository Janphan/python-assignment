str1 = input("Enter a string: ")
str_set = set(str1)

if len(str1) == len(str_set):
    print("No duplicates")
else:
    print("Contains duplicate(s)")