sellPrice = int(input("Enter the car's selling price: "))
if sellPrice < 50000:
    bonus = sellPrice*0.01
    if bonus > 200:
        print(f"The bonus is {bonus:.2f} euros.")
    else:
        print("The bonus is 200.00 euros.")
else:
    bonus = sellPrice*0.015
    print(f"The bonus is {bonus:.2f} euros.")
