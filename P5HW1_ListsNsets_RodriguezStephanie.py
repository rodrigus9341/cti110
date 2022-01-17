

# Creating lists and sets using functions
# 11/19/2021
# CTI-110 P5HW1 - Lists and Sets
# Stephanie Rodriguez
#

num = 0 
num_list = []

CREATE_LIST_CHOICE = 1
DISPLAY_RESULTS_CHOICE = 2
EXIT_CHOICE = 3


def main():

##    nums = get_list() 
##    small, large, add, avg = results(num_list)
##    eval_num(num_list, small, large, add, avg)

    choice = 0 #choice variable

    while choice != 3:

        menu() #displays the menu

        choice = int(input("Enter your choice from the menu above: "))

        if choice == 1:

            nums = get_list()
            print(num_list)


        elif choice == 2:

            if len(num_list) == 0:

                 print("NO LIST CREATED!")

            else: 

                small, large, add, avg = results(num_list)
                eval_num(num_list, small, large, add, avg)

        elif choice == 3:

            print("Program Terminated!")

        else:

            print("Error: Invalid Entry! Please Try Again!")


    
 
def get_list():

    for num in range(1,10+1): #loop is used to obtain ten numbers

        num += 0 #running total for total amount of numbers

        nums = int(input("Enter number {}: ".format(num)))

        num_list.append(nums) #each number entered is added to a list

    return nums


def results(num_list):

    small = min(num_list) #lowest number in list

    large = max(num_list) #greatest number in list

    add = sum(num_list) #adds all numbers obtained in get_list

    avg = sum(num_list) / len(num_list) #average of numbers

    return small, large, add, avg
    

def eval_num(num_list, small, large, add, avg):

    print("\n")
    print("Created list: ")
    print(num_list)

    print("Smallest number in list: " , small )

    print("Largest number in list: " , large)

    print("Sum of numbers in list: " , add)

    print("Average of numbers in list: " , avg)
    print("\n")

    num_set = set(num_list) #turns the list into a set

    print("Created set: ")
    print(num_set)

def menu():

    print('-----------MENU-------------')
    print("1) Create List")
    print("2) Display Results")
    print("3) Exit")
    print("----------------------------")
   
  


if __name__ == '__main__':
    main()

