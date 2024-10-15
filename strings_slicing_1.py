str = input("Enter a string: ")
print(str[0:2])
list = list(str)
# print(list)
str2 = ""
for c in range(0, len(list), 2):
    str2 += list[c]
print(str2)