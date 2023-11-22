# Enter two number and perform all arithmatic operation
class calculate:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        calculate.sum = x+y
        calculate.sub = x-y
        calculate.mul = x*y
        calculate.div = x/y
        calculate.mod = x%y
        calculate.exp = x**y

    def display(self):
        print("The sum of the two number is%d"%calculate.sum)
        print("The substraction of the two number is%d"%calculate.sub)
        print("The multiplication of the two number is%d"%calculate.mul)
        print("The division of the two number is%d"%calculate.div)
        print("The modulus of the two number is%d"%calculate.mod)
        print("The Exponetiation of the two number is%d"%calculate.exp)
res = calculate(x=int(input("Enter 1st number")),y=int(input("Enter 2nd number")))
res.display()
         
        