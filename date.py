from datetime import datetime, timedelta

# Function to display the current date and time
def display_current_datetime():
    now = datetime.now()
    print("Current Date and Time:")
    print(now.strftime("%Y-%m-%d %H:%M:%S"))
    print(now.strftime("%A, %B %d, %Y"))
    print(now.strftime("%I:%M %p"))

# Function to calculate the difference between two dates
def date_difference(date1, date2):
    delta = date2 - date1
    return delta.days

# Display the current date and time
display_current_datetime()

# Define two dates
date1 = datetime(2022, 7, 25)
date2 = datetime(2024, 7, 25)

# Calculate the difference between the two dates
days_difference = date_difference(date1, date2)

# Print the difference in days
print(f"\nDifference between {date1.strftime('%Y-%m-%d')} and {date2.strftime('%Y-%m-%d')} is {days_difference} days.")
