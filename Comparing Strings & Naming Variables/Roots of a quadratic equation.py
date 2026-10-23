A = int(input("Enter the coefficient of x^2: ")) # coefficient of x^2
B = int(input("Enter the coefficient of x: ")) # coefficient of x
C = int(input("Enter the constant term: ")) # constant term

r1 = (-B + ((B ** 2 - (4 * A * C)) ** 0.5)) / (2 * A) # First root
r2 = (-B - ((B ** 2 - (4 * A * C)) ** 0.5)) / (2 * A) # Second root

print(round(r1, 2)) # First root
print(round(r2, 2)) # Second root