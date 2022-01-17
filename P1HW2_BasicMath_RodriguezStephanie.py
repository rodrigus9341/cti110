

# Expense Calculator

# 9/22/21

# CTI-110 P1HW2 - Basic Math

# Stephanie Rodriguez

#

expense = input('Enter name of expense:')


monthly_charge = int(input('Enter monthly charge:'))

print('\n')
                     
monthly_tax = monthly_charge * .06
                     

total_monthly = monthly_tax + monthly_charge


total_annual = total_monthly * 12



print('Bill:' , expense , ' --------- Before Tax: ' , '$' , format(monthly_charge, '.1f'), sep='')

print('Monthly Tax:  ' , '$' , format(monthly_tax, '.2f'), sep='')

print('Monthly Charge:  ' , '$' , format(total_monthly, '.2f'), sep='')

print('Annual Charge:  ' , '$' , format(total_annual, '.2f'), sep='')
