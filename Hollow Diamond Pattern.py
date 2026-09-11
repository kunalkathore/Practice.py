n = int(input("Enter the number of rows for the hollow diamond pattern: "))


#----- hollow diamond top point

left_spaces_count = n - 1 
left_spaces = " " * left_spaces_count
print(left_spaces + "*")


#----- hollow diamond upper part 

hollow_spases_count = -1
for row in range(2, n + 1):
    left_space = " " * (n - row)
    hollow_spases_count = hollow_spases_count + 2
    hollow_spases = " " * hollow_spases_count
    print(left_space + "*" + hollow_spases + "*")


#----- hollow diamond middle part

for row in range(1, n - 1):
    left_space = " " * (row)
    hollow_spases_count = hollow_spases_count - 2
    hollow_spases = " " * hollow_spases_count
    print("Hollow diamond pattern:", left_space + "*" + hollow_spases + "*")


#----- hollow diamond bottom point

left_spaces_count = n - 1 
left_spaces = " " * left_spaces_count
print("Hollow diamond pattern:", left_spaces + "*")