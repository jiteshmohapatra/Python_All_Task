a = 15
b = 25
c= 2
if a<=b <=c:
    print(a,b,c)
elif a<=c <=b:
    print(a,c,b)

elif b<=a <=c:
    print(b,a,c)
elif b<=c <=a:
    print(b,c,a)
elif c<=a <=b:
    print(c,a,b)
else:
    print(c,b,a)



# using OOPS way


class check:
    def __init__(self,num1,num2,num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
    def display(self):
        if self.num1<=self.num2 <=self.num3:
            print(self.num1,self.num2,self.num3)
        elif self.num1<=self.num3 <=self.num2:
            print(self.num1,self.num3,self.num2)
        elif self.num2<=self.num1 <=self.num3:
            print(self.num2,self.num1,self.num3)
        elif self.num2<=self.num3 <=self.num1:
            print(self.num2,self.num3,self.num1)
        elif self.num3<=self.num1 <=self.num2:
            print(self.num3,self.num1,self.num2)
        else:
            print(self.num3,self.num2,self.num1)
res = check(num1=int(input("Enter 1st number")),num2=int(input("Enter 2nd second number")),num3=int(input("Enter another number")))
res.display()

            
            

        
