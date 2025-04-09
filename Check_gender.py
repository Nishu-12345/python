age =16
gender="Female"
if age >= 18:
    if gender == "Male":
        print("You are an adult Male")
    elif gender == "Female":
        print("You are an adult Female")
    else:
        print("You've provided the wrong gender")
else:
    print("You are not an adult")