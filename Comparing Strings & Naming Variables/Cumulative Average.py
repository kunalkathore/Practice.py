numbers = int(input("Enter the number of values: "))
total = 0

for num in range(1, numbers + 1):
    nums = int(input("Enter a number: "))
    total = total + nums
    average = total / num
    print(round(average, 3))