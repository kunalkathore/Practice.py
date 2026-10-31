n = int(input(" Enter the number of rows for the diamond: "))

# Top half: N rows
for i in range(1, n + 1):
    print(" " * (n - i) + "/" + " " * (2 * (i - 1)) + "\\")

# Bottom half: N rows
for i in range(n, 0, -1):
    print(" " * (n - i) + "\\" + " " * (2 * (i - 1)) + "/")