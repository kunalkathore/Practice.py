x = float(input("Enter a number: "))
number = int(input("Enter the power: "))

sum_of_number = 0

for power in range(1, number + 1):
    term = x ** power
    sum_of_number += term

print(round(sum_of_number, 4))