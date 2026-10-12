numbers = int(input("How many numbers do you want to sum? "))

running_total = 0

for i in range(numbers):
    num = int(input("Enter a number: "))
    running_total += num

    print(running_total)
