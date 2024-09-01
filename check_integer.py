try:
    input = input("Enter an integer: ")
    input_int = int(input)
except ValueError:
    print(f"\'{input}\' is not an integer")
else:
    print("Ok")