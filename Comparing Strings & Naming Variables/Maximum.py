number =int(input(" Enter the number of inputs: "))

max_so_far = 0

for i in range(number):
    num = int(input(" Enter a number: "))

    if num >= max_so_far:
        max_so_far = num
    print(max_so_far)    
   