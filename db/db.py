from pymongo import MongoClient

from message.base_message import Message

client = MongoClient('localhost', 27017)
db = client["test_db"]
car_collection = db["car_collection"]


def setup_schema():
    global db
    if "test_db" not in client.list_database_names():
        db = client["test_db"]
    global car_collection
    if "car_collection" not in db.list_collection_names():
        car_collection = db.create_collection("car_collection")


def get_mongo_client():
    return client


def add_car_location(message: Message):
    car_collection.update({"key": message.key}, {"$push": {"locations": message.value}}, upsert=True)


def get_car_data_for_key(key: str):
    rec = car_collection.find_one({"key": key})
    if rec is None:
        resp = {"locations": []}
    else:
        resp = {"locations": rec["locations"]}
    return resp
