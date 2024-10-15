string_input = input("Enter a string: ")
digit_list = []
count = 0
total = 0
for d in string_input:
    if d.isdigit():
        digit_list.append(d)
        d = int(d)
        total += d
count = len(digit_list)
if count == 0:
    print(f"\nThe sum of digits is {count}")
else:
    print(f"\nThe sum of digits is {total}")
    
