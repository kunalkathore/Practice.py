m = int(input("Enter the starting number: "))
n = int(input("Enter the ending number: "))

total = 0

for num in range(m, n + 1):
    total += num
    
count = n - m  + 1
average = total / count

print(total)
print(average)