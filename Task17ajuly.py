# Enter the length and breath of a rectangle find its perimeter and area

class rectangle:
    def __init__(self,l,b):
        self.l = l
        self.b = b
        rectangle.peri = 2*l+b
        rectangle.area = l*b

    def shown(self):
        print("The perimeter of a rectangle is %d"%rectangle.peri)
        print("The area of a rectangle is %d"%rectangle.area)
res = rectangle(l=int(input("Enter the length of a rectangle")),b=int(input("Enter the breath of a rectangle")))
res.shown()


        