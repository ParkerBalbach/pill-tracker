from datetime import datetime
import json

current_time = datetime.now()
dt_string = current_time.strftime("%m/%d/%Y %H:%M:%S")
pill_history = []

# what pill taken
pill_taken = input("What pill did you take? ")

# put in list then print
pill_history.append(pill_taken + ':' + ' ' + dt_string)
print(pill_taken + ':' + ' ' + dt_string)

# ask whether to see pill history
question = input("Would you like to see your pill history? ")

if question == 'y':
    print(pill_history)

elif question == 'n':
    print("goodbye!")

# ToDo - research python json and then add functionality
   


