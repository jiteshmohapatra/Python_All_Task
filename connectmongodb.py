#if you connect python with mongodb we need to install pymongo

import pymongo
client = pymongo.MongoClient('mongodb://127.0.0.1:27017')

#Create operation

mydb = client['ibmadit']

#create collection

mycol=mydb["ai"]

#Create a document inside collection

'''mydoc = {"Name":"Jitesh mohapatra","Age":23,"City":"BBSR","Pin":751010}'''

#How to insert the document in collection

'''res = mycol.insert_one(mydoc)
print(client.list_database_names())'''

#read operation

'''record = mycol.find_one()
print(record)'''

#how to update the document

'''query = {"Age":23}
new_val = {"$set":{"Age":24}}
new_doc = mycol.update_one(query,new_val)
print(new_doc)'''

#reading document after updating 
'''
doc_update = mycol.find_one()
print(doc_update)
'''
#How to delete the document


query_del = {"Pin":751010}
doc_del = mycol.delete_one(query_del)

#reading document after successfully deleting

x = mycol.find_one()
print(x)