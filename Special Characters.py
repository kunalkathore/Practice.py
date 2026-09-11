string = input("Enter a string: ") # Input for the string
vowels = "aeiouAEIOU"
v_count = 0
c_count = 0

# Count the number of vowels and consonants in the string
for char in string:
    if char.isalpha():

        # Check if the character is a vowel or consonant
        if char in vowels:
            v_count += 1
        else:
            c_count += 1 
            
print("Number of vowels:", v_count)
print("Number of consonants:", c_count)