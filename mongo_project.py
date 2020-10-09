import pymongo
import os

from os import path
if path.exists("env.py"):
    import env 


MONGO_URI = os.environ.get('MONGO_URI')
DBS_NAME = 'myTestDB'
COLLECTION_NAME = 'myFirstMDB'


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print('Could not connect to Mongo: %s') % e


def show_menu():
    print('')
    print('1. Add record')
    print('2. Find a record bt name')
    print('3. Update a record')
    print('4. Delete a record')
    print('5. Exit')

    option = input("Enter option: ")
    return option

def add_record():
    print('')
    first = input('Enter first name >')
    last = input('Enter last name >')
    dob = input('Enter date of birth >')
    gender = input('Enter gender >')
    hair_colour = input('Enter hair colour >')
    occupation = input('Enter occupation >')
    nationality = input('Enter nationality >')

    new_doc = {'first': first.lower(), 'last': last.lower(), 'dob': dob, 'gender': gender, 'hair_colour': hair_colour, 'occupation': occupation, 'nationality': nationality}

    try:
        coll.insert_one(new_doc)
        print('')
        print('Document inserted')
    except:
        print('Error accessing the database')


def main_loop():
    while True:
        option = show_menu()
        if option == '1':
            add_record()
        elif option == '2':
            print('You have selected option 2')
        elif option == '3':
            print('You have selected option 3')
        elif option == '4':
            print('You have selected option 4')
        elif option == '5':
            conn.close()
            break
        else:
            print('invalid option')

conn = mongo_connect(MONGO_URI)
coll = conn[DBS_NAME][COLLECTION_NAME]

main_loop()