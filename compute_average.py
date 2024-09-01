try: 
    number = float(input("Enter first number: "))
    sum = 0
    count = 0
    avg = 0
    while number != 0:
        sum = sum + number
        number = float(input("Enter next number: "))
        count += 1
        # print(sum)
        if number == 0:
            break
    avg = sum/count
    print(f"The average is {avg:.2f}")
except ZeroDivisionError:
    print("Nothing to be calculated")