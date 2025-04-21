from datetime import datetime 
import random

birthYear = int(input("Enter your birth year :"))
age = datetime.now().year - birthYear

lifespan = age

Jobtype = int(input("Enter your job type (1- Desk)  (2-field): "))

if Jobtype == 1:
 lifespan += random.randint(0,5)
else:
 lifespan += random.randint(5,15)

drink = input("do you drink? (y/n): ")
if drink == "y":
 if lifespan > age:
     lifespan -= random.randint(0,5)
else:
  lifespan += random.randint(5, 15) 

activity = input("do you exercise? (y/n) : ")
if activity == "y":
  lifespan +=random.randint(5,15)
else:
  lifespan += random.randint(0,15)

activity = input("do you eat green vagetables? (y/n) : ")
if activity == "y":
  lifespan +=random.randint(10,15)
else:
  lifespan +=random.randint(0,10)

  activity = input("do you eat nonvage? (y/n): ")
  if activity == "y":
    lifespan += random.randint(0,7)
  else:
    lifespan += random.randint(5,10)

print(f"you have{lifespan}year left in your life. ")