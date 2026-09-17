n = int(input("Enter the number of rows: ")) # - Input for the number of rows

# - Print the hollow diamond pattern of zeros
for row in range(1, n + 1):
    if row == 1:
        print("* " * (n * 2))
    else:
        stars = "* " * ((n - row) + 1)
        spaces = "  " * ((row * 2) - 2)
        print(stars + spaces + stars)

# - Print the bottom half of the hollow diamond pattern of zeros
for row in range(1, n + 1):
    if row == 1:
        space = "  " * ((n - row) * 2)
        print("* " + space + "* ")
    else:
        stars = "* " * row
        spaces = "  " * ((n - row) * 2)
        print(stars + spaces + stars)