number_surname = int(input("How many surnames? "))
surname = input("Enter a surname: ")
surname_list = []
surname_list.append(surname.capitalize())
for i in range(number_surname - 1):
    surname = input("Enter a surname: ")
    surname_list.append(surname.capitalize())
nonduplicated_list = sorted(set(surname_list))
print("")
print(*nonduplicated_list)