L = ["5", "eat", "9.80", "Water", "python", "-678", "7685.26", "-2.5", "sing"]

string = input() # Enter the element to search for

is_present = False

for each_item in L:
    if each_item == string:
        is_present = True

        break
