list = []
number_of_index = int(input("How many integers? "))
integer = int(input("Enter an integer: "))
list.append(integer)
for i in range(number_of_index-1):
    integer = int(input("Enter an integer: "))
    list.append(integer)
list.reverse()
print("")
print(*list)