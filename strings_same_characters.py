from collections import Counter
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
str1 = str1.replace(" ", "")
str2 = str2.replace(" ", "")
if Counter(str1) == Counter(str2):
    print("Same characters")
else:
    print("Different characters")