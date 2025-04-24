# -*- coding: utf-8 -*-
import time 
from random import randint
for i in range (1, 85):
    print('')
    space = '' 
    for i in range(1, 10):
        count = randint (1, 100)
    while count>0:
            "space += ' '" #Add actual space characters
            count -= 1
    if(i%10 == 0):
        print(space +"Happy birthday")
    elif(i%9 == 0):
        print(space +"💖🎉🍬🍫🌹") 
    # elif(i%8 == 0):
    #     print(space +"✨")
    # elif(i%7 == 0):
    #     print(space +"🍬")  
    # elif(i%6 == 0):
    #     print(space +"🍫")   
    # elif(i%5 == 0):
    #     print(space+"🌹")
    # elif(i%4 == 0):
    #     print(space+"💝")  
    # elif(i%3 == 0):
    #     print(space +"🥰")   
    else:
        print(space +"🎉HAPPY BIRTHDAY TO YOU")       
    time.sleep(0.1)   