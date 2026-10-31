word = str(input("Enter a word: "))

string = ""

for char in word:
    string += char + "-"
    
print(string[:-1])