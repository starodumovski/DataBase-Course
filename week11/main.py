import pymongo.database
from pymongo import MongoClient


def cuisine_indian(datab: pymongo.database.Database):
    cursor = datab.restaurants.find({'cuisine': 'Indian'})
    for cur in cursor:
        print(cur)


def cuisine_indian_and_thai(datab: pymongo.database.Database):
    # cursor = datab.restaurants.find({'cuisine': 'Indian' and 'Thai'})
    cursor = datab.restaurants.find({'cuisine': {'Indian', 'Thai'}})
    for cur in cursor:
        print(cur)
# print(cursor)


if __name__ == "__main__":
    client = MongoClient("mongodb://localhost")
    db = client['test_lab']
    cuisine_indian_and_thai(db)
