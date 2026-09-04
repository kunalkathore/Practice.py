n = int(input("Enter the number of inputs: "))
s = float(input("Enter the expected sum: "))

total = 0

for i in range(n):
    total += float(input("Enter a number: "))
    
if round(total, 3) == s:
    print(True)
else:
    print(False)