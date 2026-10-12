string = input("Enter a string: ")

resultant_string = ""

for char in string:
    resultant_string += char + "," # Add each character followed by a comma 

resultant_string = resultant_string[:-1]  # Remove the trailing comma

print(resultant_string)