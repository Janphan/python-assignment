apple = int(input("How many apples? "))
children = int(input("How many children? "))
applesPerChild = apple // children
leftover = apple % children
print(f"\nEach child will get {applesPerChild} apples.")
print(f"There will be {leftover} leftover apples.")