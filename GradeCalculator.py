score = int(input("What score did you get on the test? "))

if score >= 90:
    print(f"A {score} got you an A!")
elif 80 <= score <= 89:
    print(f"An {score} got you a B!")
elif 70 <= score <= 79:
    print(f"A {score} got you a C!")
elif 60 <= score <= 69:
    print(f"A {score} got you a D.")
else:
    print(f"A {score} got you an F.")

    
