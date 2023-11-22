# Write a python function to check a number is prime or not
'''num = int(input("Enter a number"))
if num>1:
    for i in range(2,num):
        if(num%i)==0:
            print(num,"Is not a prime number")
            print(i,"times",num//i,"is",num)
            break
        else:
            print(num,"Is a prime number")
    else:
        print(num,"Is not a prime number")'''


#Write a short python program to check wheather a square root of a number is prime or not


'''num = int(input("Enter a number"))
import math
a = int(math.sqrt(num))
b = 0
for i in range(2,a):
  if a%i==0:
      b = b+1
if b==0:
    print(a ,"is a prime number")
else:
    print(a, "is not a prime number")


'''


# In Python find the factorial number


'''import math
def check(n):
    return math.factorial(n)

num = int(input("Enter a number"))
f = check(num)
print("The factorial of these number is ",f)'''

#Python Program to Find the Sum of Natural Numbers
'''
num = int(input("Enter a number: "))  
  
if num < 0:  
   print("Enter a positive number")  
else:  
   sum = 0  
   # use while loop to iterate un till zero  
   while(num > 0):  
       sum += num  
       num -= 1  
   print("The sum is",sum)  
'''


# Python Program to Print the Fibonacci sequence

n = int(input ("Enter the number you want to print: "))     
# Take input from user that how many numbers you want to print  
a = 0    
b = 1    
for i in range(0,n):  
    print(a, end = " ") #a=0,a=1,a=2             
    c = a+b    #c=0+1=1,c=1+1=2,c=1+2=3,                
    a = b      #a =1,a=1 ,a=2    
    b = c       #b=1,b=2,b=3  

# Check amstrong number or not 


a = int(input("Enter a number"))

