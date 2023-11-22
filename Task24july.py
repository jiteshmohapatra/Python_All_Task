#Q)Count odd and even nos with in a given list using loops

list1=[3,4,8,10,13,14,16,15,17,22,19,23]
count_even = 0
count_odd = 0
for num in list1:
    if num%2==0:
        count_even+=1
    else:
        count_odd+=1
print("The even number are in a list is ",count_even)
print("The odd number are in a list is ",count_odd)
