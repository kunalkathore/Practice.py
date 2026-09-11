n = int(input("Enter the number of rows: ")) # Input for the number of rows

# Print the palindromic number pattern
for i in range(1, n + 1):
    s = ""

    for j in range(1, i + 1):
        s += str(j)

    for j in range(i - 1, 0, -1):
        s += str(j)

    print(s)