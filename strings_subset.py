def strings_subset():
    # Input two strings from the user
    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")
    
    # Check if the second string is empty
    if str2 == "":
        print("Nothing to be checked")
        return

    count = 0
    # Loop through each character in str2
    for char in str2:
        if char in str1:
            count += 1
        else:
            print("Not subset")
            return
    if count == len(str2):
        print("Subset")

# Call the function
strings_subset()
