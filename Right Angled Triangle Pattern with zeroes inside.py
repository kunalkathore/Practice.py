n= int(input("Enter the size of the right angled triangle: ")) # Input for the size of the right angled triangle

# right angled triangle pattern with zeroes inside
for i in range(1, n + 1):
    if 1==i:
        row = ". " * i
    elif i==n:
        row = ". " * n
    else:
        spaces = i - 2
        row = ". " + "0 " * spaces + ". "
    print(row)