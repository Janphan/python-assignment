number = int(input("Enter an integer: "))
sum = 0
if number <= 0:
    print("Nothing to be printed")
else:
    for i in range(number, 0, -1):
        sum += i
        print(i, end=" ")
    print(f"\nThe sum is {sum}")
