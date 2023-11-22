# Print the sum of Key value pair in a given dictionary

dict1 = {1:10,2:20,3:30,4:45,5:55}
#print(dict1["id1"]+dict1["id2"]+dict1["id3"]+dict1["id4"]+dict1["id5"])
x = list(dict1.keys())
y = list(dict1.values())
res = []
for i in range(0,len(x)):
    res.append(x[i]+y[i])
for i in res:
    print(i,end="")







