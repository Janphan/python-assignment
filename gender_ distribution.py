try: 
    female = int(input("Enter the number of female students: "))
    male = int(input("Enter the number of male students: "))
    total = female + male
    percentFemale = (female)/total*100
    percentMale = 100-percentFemale
    print(f"\nFemale: {percentFemale:.1f} %")
    print(f"Male: {percentMale:.1f} %")
except ValueError:
    print("The entered value is not an integer")
except ZeroDivisionError:
    print(f"\nFemale: 0.0 %")
    print(f"Male: 0.0 %")