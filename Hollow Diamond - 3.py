n = int(input("Enter the number of rows: ")) #----- Input for the number of rows
alpha = 65

#----- Print the hollow diamond pattern of alphabets
for row in range(n):
    left_spaces = " " * ((n - row) - 1)
    hollow_spaces = " " * ((2 * row) - 1)
    
    #----- Print the top half of the hollow diamond pattern
    if row == 0:
        each_row = left_spaces + chr(alpha)
        alpha += 1 
    else:
        each_row = left_spaces + chr(alpha) + hollow_spaces + chr(alpha)
        alpha += 1 
    print(each_row)
    
alpha -= 2 #----- Adjust the alpha value for the bottom half

#----- Print the bottom half of the hollow diamond pattern
for row in range(1, n):
    left_spaces = " " * row
    hollow_spaces = " " * (2 * (n - row - 1) - 1)

    #---- Print the bottom half of the hollow diamond pattern
    if row == n - 1:
        each_row = left_spaces + chr(alpha)
    else:
        each_row = left_spaces + chr(alpha) + hollow_spaces + chr(alpha)
        alpha -= 1 
    print(each_row)