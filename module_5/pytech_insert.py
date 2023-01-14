from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:admin@cluster0.lfgm4yz.mongodb.net/pytech", 27017)

db = client["mydb"]

pytech = db["PyTech"]

records = [
    {
        "student_id": "1007",
        "first_name": "Jeff",
        "last_name": "Pilcher"
    },
    {
        "student_id": "1008",
        "first_name": "John",
        "last_name": "Henry"
    },
    {
        "student_id": "1009",
        "first_name": "James",
        "last_name": "Hancock"
    }
]

pytech.delete_many({})

for record in records:
    new_student_Id = pytech.insert_one(record).inserted_id
    #print(new_student_Id)
    
docs = pytech.find()

for doc in docs:
   print(doc)
