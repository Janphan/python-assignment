while True:
    try:
        month_input = input("Enter a month number: ")
        month_number = int(month_input)
        if 1<= month_number <= 12:
            print("OK")
            break
        else:
           print(f"{month_input} is not a valid month number")
           print("")
    except (ValueError, TypeError) as e:
        print(f"\'{month_input}\' is not a valid month number")
        print("")
