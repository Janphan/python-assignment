def positive_sum(list): 
    sum = 0
    for i in range(len(list)):
        if list[i] > 0:
            sum += list[i]
    return sum
def main():
    list = []
    for i in range(5):
        number = int(input("Enter an integer: "))
        list.append(number)
    sum = positive_sum(list)
    
    print(f"\n{sum}")
if __name__ == "__main__":
    main()
