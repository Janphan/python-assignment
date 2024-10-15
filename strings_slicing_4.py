str1 = input("Enter a string: ")
if str1[::1] == str1[::-1]:
    print("Yes")
else:
    print("No")
