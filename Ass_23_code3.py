class Numbers:

    def __init__(self):
        self.Value = int(input("Enter The Number :"))

    def ChkPrime(self):
        for i in range(2,self.Value):

            if(self.Value % i == 0):
                print(f"{self.Value} not Prime Number")
                return
            
        print(f"{self.Value} is Prime Number")

    def Factors(self):
        self.Factors = []

        for i in range(1,self.Value+1):
            if self.Value % i == 0:
                self.Factors.append(i)

        print(f"{self.Value} factors are :{self.Factors}")

    def SumFactors(self):
        self.sum = 0

        for i in range(1,self.Value):
            if(self.Value%i==0):
                self.sum = self.sum + i
        print("Sum is:",self.sum)

    
    def ChkPerfect(self):
        if (self.sum == self.Value):
            print(f"{self.Value} is Perfect Number")

        else:
            print(f"{self.Value} is not Perfect Number")
                

obj1 = Numbers()
obj1.ChkPrime()
obj1.Factors()
obj1.SumFactors()
obj1.ChkPerfect()
