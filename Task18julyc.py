#Q)wap in python oops to check wheather a number is divisible by 7

class check:
    def __init__(self,num):
        self.num = num
    def display(self):
        if self.num%7==0:
            print("the number is divisible by seven")
        else:
            print("the number is not divisible by seven")

res = check(num=int(input("Enter a number")))
res.display()
        