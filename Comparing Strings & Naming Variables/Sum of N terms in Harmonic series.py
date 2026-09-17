n  = int(input()) # - Get the number of terms in the harmonic series from user input and convert it to an integer

total = 0 # - Initialize a variable to store the sum of the harmonic series

for num in range(1, n + 1): # - Loop through numbers from 1 to n (inclusive) to calculate the sum of the harmonic series
    total += 1 / num # - Add the reciprocal of the current number to the total sum
    
print(round(total, 2))