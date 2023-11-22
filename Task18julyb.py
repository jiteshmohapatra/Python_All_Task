#Q)Wap in python oops to find the smallest of three numbers
class check:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def display(self):
        if self.a<self.b and self.a<self.c:
            print("The 1st number is smallest")
        elif self.b<self.a and self.b<self.c:
            print("The second number is smallest")
        else:
            print("the last number is smallest")
res = check(a=int(input("Enter 1st number")),b=int(input("Enter 2nd number")),c=int(input("Enter 3rd number")))
res.display()
    
    