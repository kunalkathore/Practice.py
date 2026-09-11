x = float(input("Enter the value of x: "))
number = int(input("Enter the number of terms: "))

sum_of_number = 0

for power in range(1, number + 1):
    term = x ** power
    sum_of_number += term

print(round(sum_of_number, 4))