# Write a python program to return multiple of 7 with in a given range 1,70 using function,...


for i in range(1,70):
    if( i%7==0):
        print(i)

#Using OOps to find mutiple of seven
print("Using OOPS Way")
class check:
    def __init__(self,num1):
        self.num1 = num1
    def display(self):
            for i in self.num1:
                if i%7==0:
                    print(i)
res = check(range(1,70))
res.display()






        
        
    
        

