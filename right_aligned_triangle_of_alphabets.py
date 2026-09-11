# Right-aligned triangle of alphabets

n = int(input("Enter the number of rows for the right-aligned triangle of alphabets: ")) #----- Input for the number of rows

alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#----- Print the right-aligned triangle of alphabets
for i in range(n):
    spaces = "  " * (n - i)
    line = ""

    #----- Add alphabets to the line
    for j in range(i + 1):
        line += alphabets[j] + " "

    print("Right-aligned triangle of alphabets:", spaces + line)