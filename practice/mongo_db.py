import pymongo

# connect ip address 
client =pymongo.MongoClient("10.0.4.76",27017)
# db switch mydb
db = client.mydb
#choose table name
collection = db.student
# search data choose find one 
std=collection.find_one({"name":"dog"})
print(std)


for i in collection.find({"name":"tady"}):
    print(i)


collections = db.all
std=collections.find_one({"no":"1"})
print(std)

for i in collections.find({"no":"3"}):
    print(i)