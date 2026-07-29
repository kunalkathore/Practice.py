m = int(input("Enter the starting number of the range: "))
n = int(input("Enter the ending number of the range: "))

odd_count = 0
even_count = 0
for num in range(m, n + 1):
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(odd_count)
print(even_count)