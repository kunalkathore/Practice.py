L = ["5", "eat", "9.80", "Water", "python", "-678", "7685.26", "-2.5", "sing"]

string = input()

is_present = False

for each_item in L:                   # if string in L:
    if each_item == string:           #     print("True")
        is_present = True             # else:
        break                         #     print("False")

print(is_present)