n = int(input("Enter the number of rows: ")) # - Input for the number of rows

# - Print the hollow diamond pattern of zeros
for row in range(1, n + 1):
    dot = ". " * (n - row)
    zero = "0 " * ((row * 2) - 1)
    print(dot + zero + dot)

# - Print the bottom half of the hollow diamond pattern of zeros
for row in range(2, n + 1):
    dot = ". " * (row - 1)
    zero = "0 " * (((n * 2) - (row * 2)) + 1) # - Calculate the number of zeros for the bottom half
    print(dot + zero + dot)