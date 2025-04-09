class phone:
    def __init__(self, name,ram, rom):
      self.name = name
      self.ram = ram
      self.rom = rom

    def sayHello(self):
      print(f"Hello{self.name}") 
    def getInfo(self):
        print(f"Nmae:{self.name}, RAM:{self.ram},{self.rom}")
p1 = phone("phone1", 8, 200) 
p2 = phone("phone2", 16, 250)       

p1.sayHello()
p2.sayHello()

p1.getInfo()
p2.getInfo()