a = eval(input("Enter a list of element"))
print("The original list element are ",a)
a[0],a[-1] = a[-1],a[0]
print("the interchange list element of 1st and last are ",a)
