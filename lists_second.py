list = []
word = input("Enter a word (quit ends): ")
list.append(word)
while (word != "quit"):
    word = input("Enter a word (quit ends): ")
    if (word != "quit"):
        list.append(word)
list.sort()
print(*list, sep="\n")
    