class Demo:
    Value = 10

    def __init__(self,No1,No2):
        self.value1 = No1
        self.value2 = No2

    def Fun(self):
        print("The Value of Instance variable from Fun:",self.value1,self.value2)

    def Gun(self):
        print("The Value of Instance variable from gun:",self.value1,self.value2)

obj1 = Demo(11,21)
obj2 = Demo(51,101)

obj1.Fun()

obj2.Fun()
obj1.Gun()
obj2.Gun()
