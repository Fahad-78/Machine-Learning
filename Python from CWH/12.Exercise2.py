import time
current_time = time.strftime('%I:%M:%S %p')
print(current_time)
# %H gives 24-hour format (00-23)
timestamp = time.strftime('%H') 

# Convert string "10" to number 10
hour = int(timestamp)
if (hour < 12):
    print("Good Morning")# print Good Morning
elif (hour == 12):
    print("Good Noon")# print Good Noon
elif (hour > 12 and hour < 17):
    print("Good afternoon")# print Good Afternoon
else:
    print("Good night")# print Good Night
