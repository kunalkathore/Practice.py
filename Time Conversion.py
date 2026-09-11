Time = str(input("Enter the time in seconds or minutes (e.g., 120S for seconds, 2M for minutes): ")) #----- Input for the time

#----- Check if the input time is in seconds or minutes
is_seconds = Time[-1] == "S"

#----- Extract the numeric part of the time input
given_time = Time[:-1]

#----- Convert the numeric part to an integer
given_time = int(given_time)

#----- Convert the time to hours based on whether it's in seconds or minutes
if is_seconds:
    seconds_to_hours = given_time / 3600
    seconds_to_hours = round(seconds_to_hours, 2)
    hours = str(seconds_to_hours)

#----- Convert the time to hours based on whether it's in seconds or minutes
else:
    minutes_to_hours = given_time / 60
    minutes_to_hours = round(minutes_to_hours, 2)
    hours = str(minutes_to_hours)
    
print("Hours:", hours + "H")
