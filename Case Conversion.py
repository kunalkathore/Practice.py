s = input("Enter a string: ").strip() # Input for the string to be converted
result = ""

# Convert the string to snake_case
for i in range(len(s)):

    # Check if the character is uppercase
    if s[i].isupper():
        if i != 0:
            result += "_"
        result += s[i].lower()
    else:
        result += s[i]

print(result)