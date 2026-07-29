n = int(input("Enter the size of the hollow square: "))

for i in range(1, n + 1):
    if i==1:
        row ="* " * n
    elif i==n:
        row = "* " * n 
    else:
        spaces = n-2
        row = "* " + "  " * spaces + "* "
    print(row)
