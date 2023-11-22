#enter the length in centimeter and convert into m and kilometer
class measure:
    def __init__(self,a):
        self.a = a
        measure.m = a/100
        measure.km = a/100000
    def display(self):
        print("th converted value in meter is %d"%measure.m)
        print("th converted value in kilometer is %d"%measure.km)
res = measure(a=int(input("Enter the length in cm")))
res.display() 

