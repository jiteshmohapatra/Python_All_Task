#Write a program to check wheather the given letter in a word is vowel or consonant
a=input("Enter a letter ")
for x in a:
    if x=='a' or x=='e' or x=='i' or x=='o' or x=='u':
        print(x,"vowel")
    else:
        print(x,"consonant")

       


# using OOPs way
class check:
   def __init__(self,num):
      self.num = num
   def display(self):
      for y in self.num:
        if y == 'a' or y=='e' or y=='i' or y=='o' or y=='u':
            print(y,"Is vowel")
        else:
            print(y,"consonant")
res1 = check(num=input("Enter a word "))
res1.display()
        
      
      
      


    
    
