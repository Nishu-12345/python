import random

while True:
    num = int(input("guess a number -"))
    c_num = random.randint(1,10)
    if (num == c_num):
        print("Winner")
        break
    else:
        print("Better luck next time")
        print("Computer number -", c_num)

        