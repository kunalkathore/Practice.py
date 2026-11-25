programming_languages_list = [
    "Python", "Java", "Ruby", 
    "C", "C++", "Go", "R", 
    "JavaScript", "Swift", 
    "PHP", "Kotlin", "Perl"
    ]

# Write your code here
n = int(input("Enter the number of indices you want to access: "))

for num in range(n):
    index = int(input("Enter the index you want to access: "))
    print(programming_languages_list[index]) 