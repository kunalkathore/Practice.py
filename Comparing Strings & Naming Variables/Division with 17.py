# Read number of inputs
n = int(input("Enter the number of integers to process: "))

# Process each of the n numbers
for _ in range(n):
    x = int(input("Enter an integer: "))
    print(x // 17)  # integer division by 17