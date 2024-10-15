from copy import deepcopy
def new_doubled_list(number_list): 
    number_multiply_by_two_list = deepcopy(number_list)
    for i in range(len(number_multiply_by_two_list)):
        number_multiply_by_two_list[i] = number_multiply_by_two_list[i]*2
    return number_multiply_by_two_list
def main():
 first_list = [1, 2, 3, 4, 5, 6]
 second_list = new_doubled_list(first_list)
 print(first_list)
 print(second_list)
main()
