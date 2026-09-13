n = int(input("Enter the number of rows: ")) #----- Input for the number of rows

#----- Print the hollow diamond pattern of zeros
for row in range(1, n + 1):
    dots = ". " * (n - row)
    zero = "0 " * ((row * 2) - 1)
    print(dots + zero + dots + dots + zero + dots) #----- Print the M shape pattern
    