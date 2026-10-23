n = int(input("Enter the number of inputs: ")) # Number of inputs

smallest_number = float('inf') # Initialize smallest_number with a large value

for num in range(n): # Loop through the range of n to take n inputs
    number = int(input("Enter a number: "))

    if number < smallest_number:  # Update smallest_number if the current number is smaller
        smallest_number = number  # update the smallest number

    print(smallest_number) # Print the smallest number among the inputs