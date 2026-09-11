m = int(input("Enter the starting number: ")) #----- Input for the starting number
n = int(input("Enter the ending number: ")) #----- Input for the ending number

total = 0
#----- Calculate the sum of numbers from m to n
for num in range(m, n + 1):
    total += num

count = n - m + 1
average = total / count

print("Total:", total)
print("Average:", average)