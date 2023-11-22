'''# Check 1st or last number in a list same or not print (True/False)
list1 = [1,2,5,3,4,5,8,6,6,7,6,10]
if list1[0]==list1[-1]:
    print("True")
else:
    print(False)'''



def fn1(x):
    if x[0]==x[-1]:
        print("True")
    else:
        print("False")
l = [1,2,3,4,5,6,4,5,6,2,7,5,1]
res = fn1(l)
