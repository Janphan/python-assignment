visit = int(input("Enter the number of days of gym visits per year: "))
priceDay = float(input("Enter price for a day pass: "))
yearlyMembership = float(input("Enter yearly membership fee: "))

totalCost = visit*priceDay
gap = yearlyMembership - totalCost

if gap == 0:
    print("\nThere is no price difference")
if gap > 0:
    print(f"\nBuying day passes is {gap:.2f} euros cheaper")
if gap < 0: 
    print(f"\nPaying the yearly membership fee is {-gap:.2f} euros cheaper")