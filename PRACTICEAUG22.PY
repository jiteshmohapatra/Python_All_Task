'''LIST1 = ['JOHN',"JOY","PETER"]
#print(LIST1[-1],LIST1[0])
#or
LIST1[1]='JITESH'
LIST1.append("Kumar")#To add a list
del LIST1[2]
print(LIST1[1:3])
print(LIST1)'''

'''#TUPLE

tuple1 = ('jitesh','raja',23,53)#Tuple is immutable
print(tuple1)
print(tuple1[-1])
print(tuple1[0:3])
print(tuple1[3:])
print(tuple1[1:])'''

'''
#Dictionary 3In dictionary is the combination of key value pair and it is represented with in braces

dict1 = {"Name":"John","age":23,"City":"Bhubaneswar","Country":"india"}
print(dict1)
print(dict1["age"])
print(dict1["Country"],dict1["age"],dict1["Name"])
#How to change value
dict1["Country"] = "USA"
print(dict1)#The value will change india to USA
'''

#[11:01] Deepneel Majumdar

#Write a program to add key to a dictionary

dict1 = {"Name":"John","age":23,"City":"Bhubaneswar","Country":"india"}
print(dict1)
dict1["PIN"] = 754160 #one wayes
dict1.update({'Email':'john@gmail.com'}) #two wayes you can use inbuilt update function
print(dict1)


#Write a python program to sum all the items in a dictionary

dict2 = {"one":1,"two":2,"three":3,"four":4,"five":5}
print(dict2)
print(dict2["one"] + dict2["two"] + dict2["three"] + dict2["four"] + dict2["five"])
print(sum(dict2.values()))#or wayes this is inbuilt
print("The sum is =",sum(dict2.values()))
#another way debugging
s = dict2.values()
print("The values are",s)
print("The sum is",sum(s))