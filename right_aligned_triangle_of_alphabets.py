n = int(input("Enter the number of rows for the right-aligned triangle of alphabets: "))

alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(n):
    spaces = "  " * (n - i)
    line = ""

    for j in range(i + 1):
        line += alphabets[j] + " "

    print(spaces + line)