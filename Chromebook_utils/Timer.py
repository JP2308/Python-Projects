import time
import datetime

# Ask user for the time delay they want to create 
hours = int(input('How many hours? '))
minutes = int(input('How many minutes? '))
seconds = int(input('How many seconds? '))

# converts each of the times into seconds
total_time = (hours * 3600) + (minutes * 60) + seconds 

while total_time > 0:
    timer = datetime.timedelta(seconds = total_time)

    print(timer, end="\r")

    time.sleep(1)
        
    total_time -=1 

print(f'Session completed after {hours} hour(s), {minutes} minutes, and {seconds} seconds')

