gigs = int(input("Number of gigs: "))
gigsPlayed = int(input("Gigs to be played with the same set of strings: "))
price = float(input("Price of a set of guitar strings: "))

leftover = gigs % gigsPlayed
if leftover == 0:
    stringNeeded = gigs//gigsPlayed
else:
    stringNeeded = (gigs//gigsPlayed)+1
totalPrice = stringNeeded*price

print(f"\nThe guitarist needs {stringNeeded} new sets of guitar strings")
print(f"The total cost is {totalPrice:.2f} euros")