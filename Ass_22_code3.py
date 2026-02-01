class Arthimetic:

    def __init__(self):
        self.value1 = 0
        self.value2 = 0
        
    def Accept(self):
       self.value1 = float(input("Enter the value of Number 1:"))
       self.value2 = float(input("Enter the value of Number 2:"))
 
    def Addition(self):
       self.Sum = 0
       self.Sum = self.value1 + self.value2
       print("Addition is :",self.Sum)

    def Substraction(self):
        self.Sub = 0
        self.Sub = self.value1 - self.value2
        print("Substraction is :",self.Sub)

    def Multiplication(self):
        self.Mul = 0
        self.Mul = self.value1 * self.value2
        print("Multiplication is :",self.Mul)

    def Division(self):
        self.Div = 0

        if self.value2 == 0:
            print("Division By Zero")

        else:
            self.Div = self.value1 / self.value2
            print("Division is :",self.Div)

    
obj1 = Arithmetic()
obj2 = Arithmetic()

obj1.Accept()
obj1.Addition()
obj1.Substraction()
obj1.Multiplication()
obj1.Division()

print("-"*50)

obj2.Accept()
obj2.Addition()
obj2.Substraction()
obj2.Multiplication()
obj2.Division()


