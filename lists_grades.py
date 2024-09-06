list = ["A", "A", "B", "A", "C", "B", "C", "F", "B", "B", "A", "A", "C", "C", "C"]
letter = input("Enter grade letter: ")

count = 0
for i in range(len(list)-1):
    if letter.upper() == list[i]:
        count += 1
percentage = count/len(list)*100
print(f"{percentage:.1f} %")