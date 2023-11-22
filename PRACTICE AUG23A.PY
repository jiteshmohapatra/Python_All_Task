#OOPS REVISIONS
#------------------#
#CONSTRUCTOR
#-------------#
class manager:
    def __init__(self,exp,name):
        self.experience = exp
        self.fullname = name
    def display(self):
        print("The name is %s having %d years of experience"%(self.fullname,self.experience))

mgrobj1 = manager(21,"Jitesh Mohapatra")
mgrobj2 = manager(45,"peterparker")
mgrobj1.display()
mgrobj2.display()

#INHERITANCE - 1
#ans- 
#---------------#.
#Very very simplistic way

class fruit:
    def taste(self):
        print("I am inside taste function")
class mango(fruit):
    def __init__(self):
        print("Inside mango class")
    def type(self):
        print("I am alphonso mango")

obj1 = mango()
obj1.type()
obj1.taste()

#Same program add destructor 
  
class fruit:
    def taste(self):
        print("I am inside taste function")
class mango(fruit):
    def __init__(self):
        print("Inside mango class")
    def type(self):
        print("I am alphonso mango")
    def __del__(self):
        print("Destroyed")

obj1 = mango()
obj1.type()
obj1.taste()
del obj1  #write this del function to call the destructor
        

#Print  Doc string comment

def xyz():
    """This is a docstring comment"""
    print("welcome")

print(xyz.__doc__)