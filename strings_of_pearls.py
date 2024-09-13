input_string = input("Enter first string: ")
list = []
count = 0
if input_string == "quit":
    print("Bye!")
else: 
    list.append(input_string.lower())
    while (input_string != "quit"):
        input_string = input("Enter next string: ")
        list.append(input_string.lower())

    for i in range(len(list)):
        if list[i] == "pearl":
            count += 1

    print("")
    print(f"{count} pearls")
    print("Bye!")