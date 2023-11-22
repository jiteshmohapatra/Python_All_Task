#Connect Mongodb With python

#1st you need to install- pip install pymongo inside the scripts folder

import pymongo

client = pymongo.MongoClient('mongodb://127.0.0.1:27017')

#Create Operation
mydb = client['course']

#create collection

mycol = mydb['tech']

#create document inside collection

mydoc = [{"Course_id":1001,"course_name":"Ai","start_date":"sep10","city":"Bhubaneswar"},{"Course_id":1002,"course_name":"java","start_date":"sep15","city":"Bhubaneswar"},{"Course_id":1003,"course_name":"Python","start_date":"sep16","city":"Bhubaneswar"},{"Course_id":1004,"course_name":"React","start_date":"sep17","city":"Bhubaneswar"},{"Course_id":1005,"course_name":"Cloud","start_date":"sep20","city":"cuttack"}]

#inserting document inside the collection

res = mycol.insert_many(mydoc)
print(client.list_database_names())

#read documents after inserting

for x in mycol.find():

    print(x)


#How to update the document


my_update = {"course_name":"Ai"}
new_val = {"$set":{"course_name":"ArtifitialIntelligence"}}
res1 = mycol.update_one(my_update,new_val)
print(res1)


#after updating how to read

for res2 in mycol.find():
    print(res2)


#how to delete the document


dele_docu = {}
dele_res = mycol.delete_many(dele_docu)

'''for res3 in mycol.find():
    print(res3)
'''

