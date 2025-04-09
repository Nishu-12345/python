class student:
    def __init__(self, name, roll, marks):
        self.name =name
        self.roll = roll
        self.marks = marks

    def getInfo(self):
        print(f"name:{self.name}, roll:{self.roll}, marks:{self.marks}")

s1 = student("student1", 12, 237)       
s2 = student("student2", 13, 987) 
s1.getInfo() 
s2.getInfo()

