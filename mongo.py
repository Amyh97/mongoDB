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
        print ('Mongo is Connected!')
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print ('Could not connect to Mongo: %s') % e


conn = mongo_connect(MONGO_URI)
coll = conn[DBS_NAME][COLLECTION_NAME]

coll.update_many({'last': 'hollis'}, {'$set': {'hair_colour': 'red'}})

documents = coll.find({'last': 'hollis'})

for doc in documents:
    print (doc)
