def common_members(list1, list2):
    if len(list1) == 0 or len(list2) == 0:
        return False
    
    for item in list1:
        if item in list2:
            return True
    
    return False

def main():
    list1 = []
    list2 = []

    result = common_members(list1, list2)
    print(result)

if __name__ == "__main__":
    main()
