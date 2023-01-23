from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:admin@cluster0.lfgm4yz.mongodb.net/pytech", 27017)

db = client["mydb"]

pytech = db["PyTech"]

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY -- ")
docs = pytech.find()

for doc in docs:
   print(doc)

print( )

records = [
    {
        "student_id": "1010",
        "first_name": "John",
        "last_name": "Doe"
    }
]

pytech.delete_many({})

for record in records:
    new_student_Id = pytech.insert_one(record).inserted_id

    print("-- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY -- ")
doc = pytech.find_one({"student_id": "1010"})
print(doc)

pytech.delete_one({"student_id":"1010"})

    
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY -- ")
docs = pytech.find()

for doc in docs:
   print(doc)