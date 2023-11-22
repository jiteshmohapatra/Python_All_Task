'''# Count the no of occurence of a specific no in a list
x = 16
count = 0
list1 = [1,2,3,4,5,10,5,11,12,10,5,4,4,15,16,17,18,19,20,3,3,1,2,2,2]
for s in list1:
    if s==x:
        count = count+1

        print(count)'''



def fn1(x,y):
    count = 0
    for s in x:
        if s==y:
            count = count+1
    return count
num = [1,2,3,5,2,5,4,6,12,13,14,15,16,17,18,18,19,4,20]
z = 18
res = fn1(num,z)
print(res)
'''
num = [1,2,3,5,2,5,4,6,12,13,14,15,16,17,18,18,19,4,20]
z = 18
d = num.count(z)
print(d)'''





        


