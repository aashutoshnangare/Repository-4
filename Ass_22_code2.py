class Demo:
    Pi = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
       self.Radius = float(input("Enter the value of radius:"))

    def CalculateArea(self):
       self.Area = 0
       self.Area = self.Pi*(self.Radius**2)

    def CalculateCircumference(self):
        self.Circumference = 0
        self.Circumference = 2*(self.Pi*self.Radius)

    def Display(self):
        print("The Value of radius is",self.Radius)
        print("The Area of circle is",self.Area)
        print("The Circumference of circle is",self.Circumference)
    
obj1 = Demo()
obj2 = Demo()

obj1.Accept()
obj2.Accept()

obj1.CalculateArea()
obj2.CalculateArea()

obj1.CalculateCircumference()
obj2.CalculateCircumference()

obj1.Display()
obj2.Display()
