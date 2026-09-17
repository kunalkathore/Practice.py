x = float(input("Enter a number: ")) # - Input for the number
number = int(input("Enter the power: ")) # - Input for the power

sum_of_number = 0

# - Calculate the sum of the series x^1 + x^2 + x^3 + ... + x^n
for power in range(1, number + 1):
    term = x ** power
    sum_of_number += term

print("Sum of the series:", round(sum_of_number, 4))