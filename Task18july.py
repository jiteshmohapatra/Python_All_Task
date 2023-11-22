# Q) Enter the temperature in celius and converted into farenheit and vice versa
class temp:
    def __init__(self,cel,f):
        self.cel = cel
        self.f = f
        temp.fare = (cel*9/5)+32
        temp.cele = (f-32)*5/9
    def display(self):
        print("The converted value in celcius to farenheit is ",temp.fare)
        print("The converted value in  farenheit to celcius is ",temp.cele)

res = temp(cel=int(input("Enter a value in celcius")),f=int(input("Enter a value in farenheit")))
res.display()

        