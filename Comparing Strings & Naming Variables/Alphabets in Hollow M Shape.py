rows = int(input("Enter the number of rows: ")) # - Input for the number of rows

# - Print the hollow M shape pattern of alphabets
for row in range(1, rows + 1):
    spaces = " " * (rows - row)

    # - Print the top half of the hollow M shape pattern
    if row == 1:
        each_row = spaces + (chr(row + 64 ) + " ") 
    else:
        hollow_spaces = "  " * (row - 2)
        each_row = spaces + (chr(row + 64) + " ") + hollow_spaces + (chr(row + 64) + " ")

    spaces_between_triangles = " " * (rows - row) # - Calculate the spaces between the two triangles of the M shape
    
    print(each_row + spaces_between_triangles + each_row)