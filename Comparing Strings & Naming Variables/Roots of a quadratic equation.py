import math
A = int(input("Enter the coefficient of x^2: ")) # Coefficient of x^2
B = int(input("Enter the coefficient of x: ")) # Coefficient of x
C = int(input("Enter the constant term: ")) # Constant term

# - Calculate the roots of the quadratic equation Ax^2 + Bx + C = 0 using the quadratic formula
r1 = (-B + math.sqrt(B ** 2 - 4 * A * C)) / (2 * A)
r2 = (-B - math.sqrt(B ** 2 - 4 * A * C)) / (2 * A)

print(round(r1, 2)) # First root
print(round(r2, 2)) # Second root