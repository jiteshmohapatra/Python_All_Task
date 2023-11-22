# Enter the Radius of a circle and find its diameter,circumference and area
class circle:
    def __init__(self,r):
        self.r = r
        circle.dia = 2*r
        circle.circum = 2*3.14*r
        circle.area = 3.14*r*r
    def display(self):
        print("The diameter of the circle is %d"%circle.dia)
        print("The circumference of the circle is %d"%circle.circum)
        print("The area of the circle is %d"%circle.area)
res = circle(r=int(input("Enter the radius of a circle")))
res.display()

    