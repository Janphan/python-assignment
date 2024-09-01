interest_rate = float(input("Enter interest rate: "))
income_tax_rate = float(input("Enter capital income tax rate: "))
deposit = float(input("Enter initial deposit: "))
year = int(input("Enter number of years: "))

#  print the balance of the account at the end of each year.


print("")
for i in range(1, year+1):
    interest = deposit*interest_rate/100
    interest_after_tax = interest*(1-income_tax_rate/100)
    deposit += interest_after_tax
    print(f"Year {i}: {deposit:.2f}")