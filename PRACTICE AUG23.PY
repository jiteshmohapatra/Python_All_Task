'''try:
    num = 50
    den = 0
    output = num/den
    print(output)
except:
    print("Error cannot divide by zero")'''


'''try:
    nos = [5,8,7,3,6] #This one is the index error because i want to access 6 no index position so it will show error
    r = nos[0]/0 # It will show cannot devided by zero error
    print(nos[6])
except ZeroDivisionError:
    print("error cannot divide by zero")
except IndexError:
    print("Error:Index is out of boundaries")'''




#Finally Block
#--------------#
#Ans- If it generates an error if it raise an exception does not matter any kind of situation finally block is executed

'''try:
    nos = [5,8,7,3,6] #This one is the index error because i want to access 6 no index position so it will show error
    
    print(nos)
except ZeroDivisionError:
    print("error cannot divide by zero")
except IndexError:
    print("Error:Index is out of boundaries")

finally:
    print("Inside finally block") # show ans'''

#we use RAISE keyword to generate an error
try:
    nos = [5,8,7,3,6]
    print(nos)
    raise NameError("Hello everyone i have just raise an exception")
except NameError:
    print("Name Error exception")
    False



