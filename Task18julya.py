# Q) WAP In python OOps to check a number is even or odd

class check:
    def __init__(self,num):
        self.num = num
        
    def display(self):
        if self.num%2==0:
            print("The number is even")
        else:
            print("The number is Odd")


res = check(int(input("Enter A given Number and Check")))
res.display()      

        
