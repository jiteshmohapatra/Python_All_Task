# Enter two number input and find their sum

a = int(input("Enter 1st number")) # int is called typecasting
b = (input("Enter 2nd number"))
'''res = a+b
print("The sum is ",res)'''
#or
x = int(a)
y = float(b)  #one is int and another is float it will display 15.0 because the intrger and float the result will be float
z = x+y
print("The sum of the two number %d and %f is %f"%(x,y,z))
#%d is for x %f for float and again %f is for z