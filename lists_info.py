list = []
for i in range(5):
    number = int(input("Enter an integer: "))
    list.append(number)
count = len(list)
min = min(list)
max = max(list)
sum = sum(list)
print(f"\ncount: {count}")
print(f"min: {min}")
print(f"max: {max}")
print(f"sum: {sum}")