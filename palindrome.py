#Q) checks the given strings is palindrome or not

a = input("Enter a string")
a = a.lower().replace(" ","") #lower means lower case replace means space remove
if a==a[::-1]:
    print("The given string is palindrome")
else:
    print("Not a palindrome")

b = "Jitesh"
print(b)
if b==b[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")