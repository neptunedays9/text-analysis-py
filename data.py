from pymongo import MongoClient


def read_raw_data():
    mongoclient = MongoClient('localhost:27017')

    db = mongoclient.textanalysisdemo
    collection = db.text
    return collection


def write_data_text_array(text_array):
    # Connection to the mongo server
    mongoclient = MongoClient('localhost:27017')
    db = mongoclient.textanalysisdemo

    collection = db.textarray

    for elem in text_array:
        collection.insert_one({'textarray': elem})


def write_data_token_frequency(dict):
    mongoclient = MongoClient('localhost:27017')
    db = mongoclient.textanalysisdemo

    collection = db.token

    for elem in dict:
        tmp = collection.find_one({'token': elem})

        if tmp:
            collection.update_one({'_id': tmp['_id']}, {'$inc': {'count': 1}})
        else:
            collection.insert_one({'token': elem, 'count': 1})


def read_dict_token():
    # Connection to the mongo server
    mongoclient = MongoClient('localhost:27017')
    db = mongoclient.textanalysisdemo

    collection = db.token
    return collection


def read_dict_textarray():
    # Connection to the mongo server
    mongoclient = MongoClient('localhost:27017')
    db = mongoclient.textanalysisdemo

    collection = db.textarray
    return collection