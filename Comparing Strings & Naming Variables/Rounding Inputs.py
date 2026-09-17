n = int(input("Enter the number of inputs: ")) # - Input for the number of inputs

# - Round and print the inputs to 2 decimal places
for i in range(n):
    num = round(float(input("Enter a number: ")), 2)
    print("Rounded number:", num)