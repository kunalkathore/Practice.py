n = int(input("Enter a number: "))
k = int(input("Enter the position of the largest factor to find: "))

# - Find the Kth largest factor of the number
for i in range(n):
    if n % (n - i) == 0:
        factors = n - i 
        k -= 1
    if k == 0:
        break
print("The Kth largest factor is:", factors) # - Print the Kth largest factor