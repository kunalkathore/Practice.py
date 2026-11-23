list1 = [1, 2, 1]
list2 = [1, 2, 1]

copy_list1 = list1.copy() # Create a copy of list1
copy_list1.reverse() # Reverse the copy of list1

if copy_list1 == list2: # Check if the reversed copy of list1 is equal to list2
    print("palindrome")
else:
    print("not a palindrome")