import pymongo 

# connect ip address 
client =pymongo.MongoClient("10.0.4.76",27017)
# db switch mydb
db = client.mydb
#choose table name
collection = db.student


for i in range(1000):
    std ={"name":"jo","by":"2000"}
    result =collection.insert_one(std)
    
    print("新增一筆: {0}".format(result.inserted_id))