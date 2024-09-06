list = []
surname = input("Enter a surname (ok ends): ")
if surname != "ok":
    list.append(surname)
while surname != "ok":
    surname = input("Enter a surname (ok ends): ")
    if surname != "ok":
        list.append(surname)
list = set(list)
print("")
if len(list) == 1:
    print(*list)
else:
    sorted_list = sorted(list)
    print(*sorted_list, sep=", ")