for I in range(5):
    print(I)
for i in range (1, 10, 2):
   
 i=0
while(i<10):
    print("hello")
    i+=1
i = 0
while True:
    i+=1
    if (i==3):
        continue
    print(i)
    if(i==100):
        break
while True:
    user_input = input("Type something.(Type quit to close)")
    if user_input.strip(). lower() == "quit":
        break
    print("You entered", user_input)