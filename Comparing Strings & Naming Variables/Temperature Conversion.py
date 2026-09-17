temp = input()

unit = temp[-1] # - Get the last character of the input string to determine the unit (C, F, or K)
value = float(temp[:-1]) # - Get the numeric value of the temperature by removing the last character and converting it to float

# - Convert the temperature based on the input unit
if unit == "C":
    C = value
    F = C * 9 / 5 + 32 # - converts 25C to 77F
    K = C + 273   # - converts 25C to 298K

    # - Convert the temperature based on the input unit
elif unit == "F":
    F = value
    C = (F - 32) * 5 / 9 # - converts 77F to 25C
    K = C + 273   # - converts 25C to 298K

    # - Convert the temperature based on the input unit
elif unit == "K":
    K = value
    C = K - 273 # - converts 298K to 25C
    F = C * 9 / 5 + 32 # - converts 25C to 77F

# - Print the converted temperatures
print(f"{round(C, 2)}C")
print(f"{round(F, 2)}F")
print(f"{round(K, 2)}K")