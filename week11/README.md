# LAB10

###### Description
If you want to use the [python code](https://github.com/StarDNA681/DataBase-Course/blob/main/week11/python-code/main.py), just change the name of the used databse in such line (in **main** function):
```python
db = client['astara']
```

- **After the program run, you will have the folowing output:**
```
***************Exercise 1***************
Ex1 files:
	- Ex1_Indian.txt
	- Ex1_Indian_and_Thai.txt
	- Ex1_on_address.txt
***************Exercise 2***************
Inserted restaurant:
	Check the 'Ex2_insert_restaurant.txt' file
***************Exercise 3***************
Ex3 files:
	1. Before:
		- Ex3_Manhattan_before.txt
		- Ex3_Thai_before.txt
	1. After:
		- Ex3_Manhattan_after.txt
		- Ex3_Thai_after.txt
***************Exercise 4***************
Ex4 files:
	1. Before:
		- Ex4_before_to_add.txt
		- Ex4_before_to_delete.txt
	1. After:
		- Ex4_after_to_add.txt
		- Ex4_after_to_delete.txt

Process finished with exit code 0
```

The below I will introduce the **links to the files** which were generated with the python-code after the running on the [**initial dataset**](https://raw.githubusercontent.com/mongodb/docs-assets/primer-dataset/primer-dataset.json)
___
## Exercise 1
```python
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
```
___
**Ex1 files:**
- [Ex1_Indian.txt](https://github.com/StarDNA681/DataBase-Course/blob/main/week11/txt-files/Ex1_Indian.txt)
- [Ex1_Indian_and_Thai.txt](https://github.com/StarDNA681/DataBase-Course/blob/main/week11/txt-files/Ex1_Indian_and_Thai.txt)
- [Ex1_on_address.txt](https://github.com/StarDNA681/DataBase-Course/blob/main/week11/txt-files/Ex1_on_address.txt)
___
## Exercise 2
```python
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
```
___
**Ex2 files:**
- [Ex2_insert_restaurant.txt](https://github.com/StarDNA681/DataBase-Course/blob/main/week11/txt-files/Ex2_insert_restaurant.txt)
___
## Exercise 3
```python
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
```
___
**Ex3 files:**
1. **Before:**
	- [Ex3_Manhattan_before.txt](https://github.com/StarDNA681/DataBase-Course/blob/main/week11/txt-files/Ex3_Manhattan_before.txt)
	- [Ex3_Thai_before.txt](https://github.com/StarDNA681/DataBase-Course/blob/main/week11/txt-files/Ex3_Thai_before.txt)
1. **After:**
	- [Ex3_Manhattan_after.txt](https://github.com/StarDNA681/DataBase-Course/blob/main/week11/txt-files/Ex3_Manhattan_after.txt)
	- [Ex3_Thai_after.txt](https://github.com/StarDNA681/DataBase-Course/blob/main/week11/txt-files/Ex3_Thai_after.txt)
___
## Exercise 4
```python
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
```
___
**Ex4 files:**
1. **Before:**
	- [Ex4_before_to_add.txt](https://github.com/StarDNA681/DataBase-Course/blob/main/week11/txt-files/Ex4_before_to_add.txt)
	- [Ex4_before_to_delete.txt](https://github.com/StarDNA681/DataBase-Course/blob/main/week11/txt-files/Ex4_before_to_delete.txt)
1. **After:**
	- [Ex4_after_to_add.txt](https://github.com/StarDNA681/DataBase-Course/blob/main/week11/txt-files/Ex4_after_to_add.txt)
	- [Ex4_after_to_delete.txt](https://github.com/StarDNA681/DataBase-Course/blob/main/week11/txt-files/Ex4_after_to_delete.txt)