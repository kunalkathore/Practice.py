L = ["apple", "78", "970.03"]

number_of_inputs = int(input("How many items would you like to add to the list? "))

for i in range(number_of_inputs):
    new_item = input("Enter an item to add to the list: ")
    L += [new_item]
    
print(L)