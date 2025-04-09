age = int(input("Enter your age: "))
# if(age>= 18):
#     print("Yes, you can vote")
# else:
#     print("Yes, you can't vote")
if(age >=0 and age < 9):
    print("You're a kids")
elif(age >=9 and age <18):
    print("You're a teen")
elif(age >= 18):
    print("You're an adult")
else:
    print("age is not correct")