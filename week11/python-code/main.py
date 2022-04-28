import datetime
import pprint as pprint
from typing import TextIO
import pymongo.database
from pymongo import MongoClient


# Printing the data from database
def print_cursor(cursor: pymongo.cursor.Cursor):
    for item in cursor:
        pprint.pprint(item)


# Printing the data from database to thr file
def print_cursor_int_file(cursor: pymongo.cursor.Cursor, descriptor: TextIO):
    for cur in cursor:
        descriptor.write(str(cur)+'\n')


# Finding Indian cuisines
def cuisine_indian(datab: pymongo.database.Database):
    cursor = datab.restaurants.find({'cuisine': 'Indian'})
    with open("Ex1_Indian.txt", 'w'):
        pass
    with open("Ex1_Indian.txt", "w") as f:
        print_cursor_int_file(cursor, f)


# Finding Indian and Thai cuisines
def cuisine_indian_and_thai(datab: pymongo.database.Database):
    cursor = datab.restaurants.find({'cuisine': {"$in": ['Indian', 'Thai']}})
    with open("Ex1_Indian_and_Thai.txt", 'w'):
        pass
    with open("Ex1_Indian_and_Thai.txt", "w") as f:
        print_cursor_int_file(cursor, f)


# Finding the restaurant on the Rogers Avenue with zipcode (11226) and building (1115)
def restaurant_on_the_address(datab: pymongo.database.Database):
    cursor = datab.restaurants.find({'address.zipcode': '11226',
                                     'address.street': 'Rogers Avenue',
                                     'address.building': '1115'})
    with open("Ex1_on_address.txt", 'w'):
        pass
    with open("Ex1_on_address.txt", "w") as f:
        print_cursor_int_file(cursor, f)


# Insert specific record in the database
def insert_data(datab: pymongo.database.Database):
    print("Inserted restaurant:")
    _id = datab.restaurants.insert_one({
        'address': {'building': '1480',
                    'coord': [-73.9557413, 40.7720266],
                    'street': '2 Avenue',
                    'zipcode': '10075'},
        'borough': 'Manhattan',
        'cuisine': 'Italian',
        'grades': [{'date': datetime.datetime(2014, 10, 1, 0, 0),
                    'grade': 'A',
                    'score': 11}],
        'name': 'Vella',
        'restaurant_id': '41704620'})
    cursor = datab.restaurants.find({'restaurant_id': '41704620'})
    with open("Ex2_insert_restaurant.txt", "w"):
        pass
    with open("Ex2_insert_restaurant.txt", "w") as f:
        print_cursor_int_file(cursor, f)
    print("\tCheck the 'Ex2_insert_restaurant.txt' file")


# Deleting the one Manhattan restaurant and all Thai cuisines
def delete_one_manhattan_and_all_thai(datab: pymongo.database.Database):
    cursor_1 = datab.restaurants.find({'borough': 'Manhattan'})
    with open("Ex3_Manhattan_before.txt", "w"):
        pass
    with open("Ex3_Manhattan_before.txt", "w") as f:
        print_cursor_int_file(cursor_1, f)
    cursor_2 = datab.restaurants.find({'cuisine': 'Thai'})
    with open("Ex3_Thai_before.txt", "w"):
        pass
    with open("Ex3_Thai_before.txt", "w") as f:
        print_cursor_int_file(cursor_2, f)
    datab.restaurants.delete_one({'borough': 'Manhattan'})
    cursor_1 = datab.restaurants.find({'borough': 'Manhattan'})
    with open("Ex3_Manhattan_after.txt", "w"):
        pass
    with open("Ex3_Manhattan_after.txt", "w") as f:
        print_cursor_int_file(cursor_1, f)
    datab.restaurants.delete_many({'cuisine': 'Thai'})
    cursor_2 = datab.restaurants.find({'cuisine': 'Thai'})
    with open("Ex3_Thai_after.txt", "w"):
        pass
    with open("Ex3_Thai_after.txt", "w") as f:
        print_cursor_int_file(cursor_2, f)
    print("Ex3 files:")
    print("\t1. Before:")
    print("\t\t- Ex3_Manhattan_before.txt")
    print("\t\t- Ex3_Thai_before.txt")
    print("\t1. After:")
    print("\t\t- Ex3_Manhattan_after.txt")
    print("\t\t- Ex3_Thai_after.txt")


# Filtering (deleting or updating) of all restaurants on the Roger Avenue
def filter_by_grades_on_rogers_avenue(datab: pymongo.database.Database, to_delete: bool):
    cursor = datab.restaurants.find({'address.street': 'Rogers Avenue'})
    data_remove = []
    data_add_c = []
    for cur in cursor:
        amount = 0
        m = cur['grades']
        for g in m:
            if g['grade'] == 'C':
                amount += 1
        if amount > 1:
            data_remove.append(cur['_id'])
        else:
            data_add_c.append(cur['_id'])
    if to_delete:
        for data in data_remove:
            datab.restaurants.delete_one({'_id': data})
        for data in data_add_c:
            datab.restaurants.update_one({'_id': data}, {"$push": {'grades': {
                'date': datetime.datetime.now(),
                'grade': 'C',
                'score': 5
            }}})
        with open("Ex4_after_to_delete.txt", "w"):
            pass
        with open("Ex4_after_to_delete.txt", "w") as f:
            for data in data_remove:
                cursor_1 = datab.restaurants.find({'_id': data})
                print_cursor_int_file(cursor_1, f)
        with open("Ex4_after_to_add.txt", "w"):
            pass
        with open("Ex4_after_to_add.txt", "w") as f:
            for data in data_add_c:
                cursor_2 = datab.restaurants.find({'_id': data})
                print_cursor_int_file(cursor_2, f)
    else:
        with open("Ex4_before_to_delete.txt", "w"):
            pass
        with open("Ex4_before_to_delete.txt", "w") as f:
            for data in data_remove:
                cursor_1 = datab.restaurants.find({'_id': data})
                print_cursor_int_file(cursor_1, f)
        with open("Ex4_before_to_add.txt", "w"):
            pass
        with open("Ex4_before_to_add.txt", "w") as f:
            for data in data_add_c:
                cursor_2 = datab.restaurants.find({'_id': data})
                print_cursor_int_file(cursor_2, f)


def run_exercises(datab: pymongo.database.Database):
    # Exercise 1:
    print("***************Exercise 1***************")
    # 1.1 Query all Indian cuisines
    cuisine_indian(datab)
    # 1.2 Query all Indian and Thai cuisines
    cuisine_indian_and_thai(datab)
    # 1.3 Find a restaurant with the following address: 1115 Rogers Avenue, 11226
    restaurant_on_the_address(datab)
    print("Ex1 files:")
    print("\t- Ex1_Indian.txt")
    print("\t- Ex1_Indian_and_Thai.txt")
    print("\t- Ex1_on_address.txt")

    # Exercise 2
    print("***************Exercise 2***************")
    # 2.1 Insert into the database following restaurant
    insert_data(datab)

    # Exercise 3
    print("***************Exercise 3***************")
    # Delete from the database a single Manhattan located restaurant and all Thai cuisines
    delete_one_manhattan_and_all_thai(datab)

    # Exercise 4
    print("***************Exercise 4***************")
    #  Query all restaurants on the Rogers Avenue street, for each of them do the following:
    # • if it has more than one C grades → delete this restaurant
    # • otherwise, add another C grade to this restaurant
    filter_by_grades_on_rogers_avenue(datab, False)
    filter_by_grades_on_rogers_avenue(datab, True)
    print("Ex4 files:")
    print("\t1. Before:")
    print("\t\t- Ex4_before_to_add.txt")
    print("\t\t- Ex4_before_to_delete.txt")
    print("\t1. After:")
    print("\t\t- Ex4_after_to_add.txt")
    print("\t\t- Ex4_after_to_delete.txt")


if __name__ == "__main__":
    client = MongoClient("mongodb://localhost")
    db = client['astara']
    run_exercises(db)
    