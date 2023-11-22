#1)PYTHON SETS
#----------------#

#(i) Collection of unique data
#(ii) data are immutable
#(ii) Non-indexed,un-ordered
#(iii) Elements cannot be duplicate

#------------------#


#How to create python sets

set1 = {69,93,45,65,78,63,32}
print(set1)
#How to add element in a sets
set1.add(100)
print(set1)
#It will show unorderd type {32, 65, 93, 69, 100, 45, 78, 63}

# How to UPDATE  The SETS

companies = {'x','y','z'}
tech_companies = ['a','b','c']

companies.update(tech_companies)
print(companies)


#JSON TO DICTIONARY & DICTIONARY TO JSON

import json
dict1 = {"Name":'Jitesh Mohapatra',"country":"India","state":"odisha","Pin":754160}

jsonvar = json.dumps(dict1)
print(jsonvar)

#This one is dictionary to json

#Count the number of occurrences of 25 from a tuple
'''
def fn1(x,y):
    count =0
    for s in x:
        if s==y:
            count = count+1
    return count
        
num = (1,2,3,5,10,25,25,36,41,25,63,25,11,3,25)
z=3
res = fn1(num,z)
print(res)
'''

#USING OOPS WAY



class check:
    
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def display(self):
        count = 0
        for i in self.a:
            if i == self.b:
                count = count+1
        return count
list1 = [1,2,3,4,5,5,6,1,4,4,5,8,10]
z =int(input("Enter a number 1 to 10"))
res = check(list1,z)
res1 = res.display()
print(res1)
                


            

    


        





        
    
        
    

    
        
    


        
        
        
