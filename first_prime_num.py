n = int(input("Enter the number of inputs: "))

# - Find the first prime number among the inputs
for i in range(n):
    num = int(input("Enter a number: "))
    count = 0

    # - Check if the number is prime
    for j in range(1, num + 1):
        if num % j == 0:
            count += 1 

    # - If the count of divisors is 2, then the number is prime
    if count == 2:
        print("First prime number:", num)
        break
