try:
    number = int(input("Enter a weekday number: "))
    if number < 1 or number > 7:
        raise ValueError("Please enter an integer between 1 and 7")
except ValueError as e:
    print("Please enter an integer between 1 and 7")
else:
    print("OK")