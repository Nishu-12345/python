# def info ():
#  print("Hello")
# info()
# info()
# info()
# info()
# info()
# def info (name, city, age):
#     print(f"hello {name}, from {city}, you're {age} year old")
# # greet(" swati ")
# # greet(" Kamni ")
# info("name","city")
# def studentInfo(name, marks, collage="ssgt"):
#     print(f"hello {name}, your {marks}, you're from {collage}")
# studentInfo("name", 200, "MIT") 
# studentInfo("name", 300, "IFTM")
# studentInfo("name", 250)  
# def add(a,b):
#     return a+b
# print(add(4,6))
# def sub(a,b):
#     print(a-b)
# sub(3475,1093465)
def sum(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b
def calc(fn, a, b):
    return fn(a, b)
print(calc(sum, 4, 3))
print(calc(sub, 12, 3))
print(calc(mul, 5, 2))
print(calc(div, 15, 3))
print(type(sum))
