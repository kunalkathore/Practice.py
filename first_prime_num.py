n = int(input("Enter the number of inputs: "))

for i in range(n):
    num = int(input("Enter a number: "))
    count = 0
    
    for j in range(1, num + 1):
        if num % j == 0:
            count += 1 
            
    if count == 2:
        print(num)
        break
