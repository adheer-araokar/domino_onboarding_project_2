from pymongo import MongoClient

from message.base_message import Message
from bson import json_util

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


def add_car_location(message: Message, host_name: str):
    rec = car_collection.find_one({"key": host_name})
    if rec is None:
        print("new"+message.key)
        car_collection.insert_one({"key": host_name, "locations": {message.key: [message.value]}})
    else:
        all_cars = rec["locations"]
        if message.key in all_cars.keys():
            locations = rec["locations"][message.key]
            locations.append(message.value)
        else:
            locations = [message.value]
        car_collection.update_one({"key": host_name}, {"$set": {"locations."+message.key: locations}})


def get_car_data_for_key(key: str):
    recs = car_collection.find({"locations."+key: {"$exists": True}})
    resp = {"locations": []}
    locations = resp["locations"]
    for rec in recs:
        if rec["locations"][key] is not None:
            locations.extend(rec["locations"][key])
    return json_util.dumps(resp)
