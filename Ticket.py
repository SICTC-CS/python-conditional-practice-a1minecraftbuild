speed = int(input("How fast were you driving? "))

birthday = input("Is it your birthday? (y/n) ")

result = 0

if birthday == "y":
    speed=speed-5

if speed <= 60:
    result = 0
elif 61 <= speed <= 80:
    result = 1
else:
    result = 2

print(result)
if result == 0:
    result = "No ticket"
elif result == 1:
    result = "Small ticket"
else:
    result = "Big ticket"

print(result)
