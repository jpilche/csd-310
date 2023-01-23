from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:admin@cluster0.lfgm4yz.mongodb.net/pytech", 27017)

db = client["mydb"]

pytech = db["PyTech"]
    
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY -- ")
docs = pytech.find()

for doc in docs:
   print(doc)

print( )

pytech.update_one({
	"student_id": "1007"	
},
{
    "$set": {
        "last_name": "Smith"
        }
});

print("-- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY -- ")
doc = pytech.find_one({"student_id": "1007"})
print(doc)

