Time = str(input("Enter the time in seconds or minutes (e.g., 120S for seconds, 2M for minutes): "))

is_seconds = Time[-1] == "S"

given_time = Time[:-1]
given_time = int(given_time)

if is_seconds:
    seconds_to_hours = given_time / 3600
    seconds_to_hours = round(seconds_to_hours, 2)
    hours = str(seconds_to_hours)
    
else:
    minutes_to_hours = given_time / 60
    minutes_to_hours = round(minutes_to_hours, 2)
    hours = str(minutes_to_hours)
    
print(hours + "H")
