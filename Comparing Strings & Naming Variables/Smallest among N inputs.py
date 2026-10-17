n = int(input()) # Number of inputs

smallest_number = 999999999 # Initialize smallest_number with a large value

for num in range(n):
    number = int(input())

    if number < smallest_number:  # Update smallest_number if the current number is smaller
        smallest_number = number  # update the smallest number

print(smallest_number) # Print the smallest number among the inputs