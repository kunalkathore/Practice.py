numbers = int(input("How many numbers do you want to sum? ")) # Prompt the user to enter the number of numbers to sum

running_total = 0 # Initialize the running total

for i in range(numbers):
    num = int(input("Enter a number: ")) # Prompt the user to enter a number
    running_total += num

    print(running_total)  # Print the current running total 