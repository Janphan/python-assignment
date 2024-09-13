def common_members(list1, list2):   
    count = 0
    if len(list1) == 0 or len(list2) == 0:
        return False
    else: 
        for i in range(len(list1)):
            for k in range(len(list2)):
                if list1[i] == list2[k]:
                    count += 1            
        if count < 1:
            return False
        else:
            return True
def main():
    # list1 = [1,2,3,4,5]
    # list2 = [1,2,4,6,7]
    list1 = []
    list2 = []

    result = common_members(list1,list2)
    print(result)
if __name__ == "__main__":
    main()