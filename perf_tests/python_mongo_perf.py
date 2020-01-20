from pymongo import MongoClient
import time


client = MongoClient('localhost', 27017)
db = client["test_db"]
test_collection = db["test_collection"]


def setup_schema():
    global db
    if "test_db" not in client.list_database_names():
        db = client["test_db"]
    global test_collection
    if "test_collection" not in db.list_collection_names():
        test_collection = db.create_collection("test_collection")


def test_insert():
    global test_collection

    start_time = time.time()

    for i in range(1000000):
        row = create_row(i)
        test_collection.insert_one(row)

    end_time = time.time()

    print(end_time - start_time)


def test_read():
    start_time = time.time()
    print(test_collection.find_one({"key78": "value78"}))
    end_time = time.time()
    print(end_time - start_time)


# order can have 1 for ASC and -1 for DESC
def create_index(field, order):
    resp = test_collection.create_index(
        [
            (field, order)
        ]
    )
    print(resp)


def create_row(id):
    # row = {"_id": id}
    row = {}
    for i in range(100):
        key = "key" + str(i)
        value = "value" + str(i)
        row[key] = value
    return row


if __name__ == '__main__':
    # setup_schema()
    # test_insert()
    # create_index("key9999", 1)
    test_read()


