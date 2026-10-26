n = int(input("Enter the number of rows for the pyramid: "))

for i in range(1, n+1):
    spaces = " "*(n - i)
    left_nums = ""
    right_nums = ""

    for j in range(1, i+1):
        left_nums = str(j) + left_nums
        right_nums = right_nums + str(j)

    print(spaces + left_nums + right_nums[1:])