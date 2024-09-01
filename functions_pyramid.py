def print_pyramid(height):
    for i in range(1, height+1):
         print(" " * (height - i) + "*" * (2 * i - 1))
def main():
    height = int(input("Enter pyramid height: "))
    print_pyramid(height)
if __name__ == "__main__":
    main()