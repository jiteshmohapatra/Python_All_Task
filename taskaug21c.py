# count the occurence of a specific value in a list
'''list1 = [1,5,"2.5","jitesh",10,"joy"]'''



#Q.3) Find the product of 2 nos. If the product value is greater than 300, then return their sum. Use function.
def check(x,y):
    if x*y>300:
        return x+y
num1 = int(input("Enter 1st numbr"))
num2 = int(input("Enter 2nd numbr"))
result = check(num1,num2)
print(result)