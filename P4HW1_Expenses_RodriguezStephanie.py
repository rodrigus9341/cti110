

#CTI-110
#P4HW1 - Expenses
#Stephanie Rodriguez
#12/1/2021


con = 'y'

start_amt = float(input("Enter starting amount in account $"))

num_exp = 0
sub = 0 # variables for expenses subtracted from account
total_exp = 0 # variable for total expenses

while con == 'y' or con == 'Y':

    print("\n")
    expense = float(input("Enter expense "+ str(num_exp+1)+": " ))
    num_exp += 1

    total_exp += expense # running total for all expenses entered
    sub = start_amt - total_exp # subtracts the total expenses from starting amount
    
    con = input("Do you want to enter another expense? (y/n): ")
    print("\n")
         
print("Amount in account before expenses subtracted $", start_amt)
print("Number of expenses entered: ", num_exp)
print("Amount in account after expenses subtracted is $", sub)
