# Q) Check if a given key already exist in dictionary 
dict1= {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def check(x):
  if x in dict1:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
check(5)
check(4)
check(10)
check(1)


