
#CTI-110

#P2HW2 - List and Sets

#Stephanie Rodriguez

#10/3/2021

#


num1 = float(input("Enter num 1: "))

num2 = float(input("Enter num 2: "))

num3 = float(input("Enter num 3: "))

num4 = float(input("Enter num 4: "))

num5 = float(input("Enter num 5: "))

num6 = float(input("Enter num 6: "))

numbers_list = ([num1, num2, num3, num4, num5, num6])

numbers_set = set([num1, num2, num3, num4, num5, num6])

print("\n")

print("Created list")
print(numbers_list)

print("Smallest number in list: " , min(numbers_list))

print("Largest number in list: " , max(numbers_list))

print("Sum of numbers in list: " , sum(numbers_list))

print("Average of numbers in list: " , sum(numbers_list) / len(numbers_list))
print("\n")

print("Created set")
print(numbers_set)




