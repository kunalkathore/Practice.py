m = int(input("Enter the starting number of the range: ")) #----- Input for the starting number of the range
n = int(input("Enter the ending number of the range: ")) #----- Input for the ending number of the range

odd_count = 0
even_count = 0
        
#----- Count the odd and even numbers in the range
for num in range(m, n + 1):
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Odd numbers:", odd_count)
print("Even numbers:", even_count)