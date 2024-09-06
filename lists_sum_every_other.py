def sum_every_other(list):
    if not list:
        return None
    sum = 0
    for i in range(0, len(list), 2):
        sum += list[i]
    return sum
def main():
    # list = [1,2,3,-3,4,8,-1]
    list = []
    
    result = sum_every_other(list)
    if result is not None:
        print(f"Sum every other in the list is {result}")
    
if __name__ == "__main__":
    main()