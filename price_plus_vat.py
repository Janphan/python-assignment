try: 
    price = float(input("Enter price: "))
    priceWithVAT = price*1.24
    print(f"The price with VAT is {priceWithVAT:.2f}")
except ValueError:
    print("Invalid price")