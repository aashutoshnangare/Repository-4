class BankAcount:
    ROI = 10.5

    def __init__(self):
        self.Name = input("Enter The Name of Holder :")
        self.Amount = float(input("Enter Account Balance :"))

    def Deposit(self):
        self.Damount = float(input("Enter The Amount to Deposit :"))
        self.Amount = self.Amount + self.Damount
        print("Deposit Amount Sucessfull")
        print(f"Account Balance :{self.Amount}")
    
    def Withdraw(self):
        self.Wamount = float(input("Enter The Amount to WithDraw :"))
        if self.Amount < self.Wamount:
            print(f"Insufficient Balance , Current Balance :{self.Amount}")

        else:
            self.Amount = self.Amount - self.Wamount
            print("Withdraw Amount Sucessfull")
            print(f" Account Balance :{self.Amount}")

    def Display(self):
        print(f"Account Holder Name :{self.Name}")
        print(f"Current Balance is :{self.Amount}")

    def CalculateInterest(self):
        self.Interest = 0.0
        self.Interest = (self.Amount * BankAcount.ROI) / 100    
        print(f"Interest is :{self.Interest}")

while True:
    print("1. Open Application")
    print("2. Close Application")
    Choice = int(input("Enter the choice :"))

    if Choice == 1:
        print("Opening The Application")
        obj1 = BankAcount()

        while True:
            print("-"*20 ,"Menu","-"*20)
            print("1. Display ")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Calculate Interest")
            print("5. Exit")

            print("-"*45)

            Choice = int(input("Enter the choice :"))
            if Choice == 1:
                obj1.Display()
            
            elif Choice == 2:
                obj1.Deposit()

            elif Choice == 3:
                obj1.Withdraw()
            
            elif Choice == 4:
                obj1.CalculateInterest()

            elif Choice == 5:
                print("Thank You For Using Application")
                print("Exiting Application...")
                break
    elif Choice == 2:
        print("Closing Application")
        break
    break
        
print("-"*45)
 
while True:
    print("1. Open Application 2")
    print("2. Close Application 2")
    Choice = int(input("Enter the choice :"))

    if Choice == 1:
        print("Opening The Application 2 ...")
        obj2 = BankAcount()

        while True:
            print("-"*20 ,"Menu","-"*20)
            print("1. Display ")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Calculate Interest")
            print("5. Exit")

            print("-"*45)

            Choice = int(input("Enter the choice :"))
            if Choice == 1:
                obj2.Display()
            
            elif Choice == 2:
                obj2.Deposit()

            elif Choice == 3:
                obj2.Withdraw()
            
            elif Choice == 4:
                obj2.CalculateInterest()

            elif Choice == 5:
                print("Thank You For Using Application")
                break

    elif Choice == 2:
        print("Closing Application")
        print("Exiting Application ...")
        break
    break
        
            