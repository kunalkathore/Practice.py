n = int(input("Enter the number of elements you want to add to the list: "))

list_a = []
for i in range(n):
    value = input("Enter the value you want to add to the list: ")
    list_a += [value]

print(list_a)



'''
n = int(input())
items = []

for _ in range(n):
    items.append(input())

print(items)

'''