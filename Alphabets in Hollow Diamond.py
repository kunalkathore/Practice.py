n = int(input("Enter the number of rows: "))                                                                            #----- Input for the number of rows

alpha = 65

# - Print the top half of the hollow diamond pattern of alphabets
for i in range(n):                                                                                                      # - Loop through each row of the top half of the hollow diamond pattern
    left_spaces = " " * (n - i - 1)                                                                                     # - Calculate the number of spaces to the left of the alphabets
    hollow_spaces = " " * (2 * i - 1)                                                                                   # - Calculate the number of spaces between the alphabets in the hollow diamond pattern

    # - Print the top half of the hollow diamond pattern of alphabets
    if i == 0:                                                                                                          # - If it's the first row, print only one alphabet
        print(left_spaces + chr(alpha))                                                                                 # - Print the first alphabet
        alpha += 1                                                                                                      # - Increment alpha for the next alphabet
    else:
        print(left_spaces + chr(alpha) + hollow_spaces + chr(alpha + 1))                                                # - Print the alphabets with spaces between them
        alpha += 2                                                                                                      # - Increment alpha for the next pair of alphabets


# - Print the bottom half of the hollow diamond pattern of alphabets

alpha -= 4 # - Adjust alpha for the bottom half

# - Print the bottom half of the hollow diamond pattern of alphabets
for i in range(1, n):                                                                                                   # - Loop through each row of the bottom half of the hollow diamond pattern
    left_spaces = " " * i                                                                                               # - Calculate the number of spaces to the left of the alphabets
    hollow_spaces = " " * (2 * (n - i - 1) - 1)                                                                         # - Calculate the number of spaces between the alphabets in the hollow diamond pattern

    # - Print the bottom half of the hollow diamond pattern of alphabets
    if i == n - 1:                                                                                                      # - If it's the last row, print only one alphabet
        print(left_spaces + chr(65))                                                                                    # - Print the last alphabet
    else:
        print(left_spaces + chr(alpha) + hollow_spaces + chr(alpha + 1))                                                # - Print the alphabets with spaces between them

    alpha -= 2 # - Adjust alpha for the bottom half