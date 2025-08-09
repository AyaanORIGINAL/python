from datetime import date, time, datetime

today = date.today()
print("Today's date is:", today)

now = datetime.now()
print("Current date and time is:", now)

print("Date components: ")
print("Year:", today.year)
print("Month: ", today.month)
print("Day:", today.day)

birthyear = int(input("Enter your birth year: "))
age = today.year - birthyear
print("Your age is:", age)