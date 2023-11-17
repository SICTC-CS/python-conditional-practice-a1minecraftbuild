Sunday = 0
Monday = 1
Tuesday = 2
Wednesday = 3
Thursday = 4
Friday = 5
Saturday = 6

dayToday=int(input("What day is it today? "))
daysElapsed = int(input("How many days will elapse? "))
daysTodayNumber = dayToday
dayTodayNumber = dayToday + daysElapsed
while dayTodayNumber > 6:
    dayTodayNumber = dayTodayNumber - 7

if dayToday == 0 or 1 or 2 or 3 or 4 or 5 or 6:
    if dayToday == 0:
        dayToday = "Sunday"
    elif dayToday == 1:
        dayToday = "Monday"
    elif dayToday == 2:
        dayToday = "Tuesday"
    elif dayToday == 3:
        dayToday = "Wednesday"
    elif dayToday == 4:
        dayToday = "Thursday"
    elif dayToday == 5:
        dayToday = "Friday"
    else:
        dayToday = "Saturday"

    print(f"Today's date is {dayToday}")
else:
    print("That is not a valid day")

dayToday = dayTodayNumber
if dayToday == 0 or 1 or 2 or 3 or 4 or 5 or 6:
    if dayToday == 0:
        dayToday = "Sunday"
    elif dayToday == 1:
        dayToday = "Monday"
    elif dayToday == 2:
        dayToday = "Tuesday"
    elif dayToday == 3:
        dayToday = "Wednesday"
    elif dayToday == 4:
        dayToday = "Thursday"
    elif dayToday == 5:
        dayToday = "Friday"
    else:
        dayToday = "Saturday"

    print(f"Your future date is {dayToday}")
else:
    print("That is not a valid day")

