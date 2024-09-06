list = []

for i in range(5):
    integer = int(input("Enter an integer: "))
    list.append(integer)
list = sorted(list, reverse=True)
print("")
print(*list, end=" ")