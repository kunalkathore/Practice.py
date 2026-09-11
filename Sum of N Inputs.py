n = int(input("Enter the number of inputs: ")) # Input for the number of inputs
s = float(input("Enter the expected sum: ")) # Input for the expected sum

total = 0

# Read n inputs and calculate their sum
for i in range(n):
    total += float(input("Enter a number: "))

# Check if the rounded sum matches the expected sum
if round(total, 3) == s:
    print("Sum matches the expected value.")
else:
    print("Sum does not match the expected value.")