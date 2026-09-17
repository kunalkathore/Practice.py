A = int(input()) # coefficient of x^2
B = int(input()) # coefficient of x
C = int(input()) # constant term

r1 = (-B + ((B ** 2 - (4 * A * C)) ** 0.5)) / (2 * A) # First root
r2 = (-B - ((B ** 2 - (4 * A * C)) ** 0.5)) / (2 * A) # Second root

print(round(r1, 2)) # First root
print(round(r2, 2)) # Second root