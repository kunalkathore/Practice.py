number = int(input("Enter the number of rows for the hollow pyramid: "))


print("|")
for i in range(1, number):
    hollow_spaces = " " * (i - 1)
    print("| " + hollow_spaces + "\\" )


for i in range(number -1, 0, -1):
    hollow_spaces = " " * (i - 1)
    print("| " + hollow_spaces + "/" )

print("|")