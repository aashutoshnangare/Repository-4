class BookStore:
    NoOfBooks = 0

    def __init__(self):
        self.Bookname = input("Enter The Name of Book")
        self.Authorname = input("Enter The Name of Author")

    
        if self.Bookname == None or self.Authorname == None:
            print("Enter The Bookname and Authorname first")

        else:
            BookStore.NoOfBooks += 1  

    def Display(self):
        print(f"The Book {self.Bookname} By Author {self.Authorname} No of Books :{self.NoOfBooks}")
            

obj1 = BookStore()
obj1.Display()

obj2 = BookStore()
obj2.Display()

    


