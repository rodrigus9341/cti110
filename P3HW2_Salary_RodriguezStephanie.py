
# CTI-110
# P3HW2-Salary
# Stephanie Rodriguez
# 10/15/2021
#

name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked: "))
pay = float(input("Enter employee's pay rate: "))

reg = pay * 40
overtime = (pay * 1.5 * (hours - 40))
gross = overtime + reg
over_hours = (hours - 40)

print("-------------------------------------")

print("Employee name: " , name)

print("\n")

print("Hours Worked\tPay Rate\tOverTime\tOverTime Pay\tRegHour Pay\tGross Pay")
print("---------------------------------------------------------------------------------------------")


if hours > 40:
    

    Overtime = (pay * 1.5 * (hours - 40))

else:
    
    
    Reg = pay * 40

print(hours,"\t\t", pay, "\t\t", over_hours, "\t\t", end="")
print(overtime,"\t\t", end="")
print("$", format(reg, ".2f"), "\t", end="")
print("$", format(gross, ".2f"))


