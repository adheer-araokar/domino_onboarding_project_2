from pymongo import MongoClient
import time
import random


def test_n_reads(collection, n, n_unique_random_ids):
    # n_unique_random_ids = random.sample(range(1, 2000000), n)
    read_times = []
    for i in n_unique_random_ids:
        start_time = time.time()
        collection.find_one({get_primary_key(): i})
        # print(test_collection.find_one({get_primary_key(): i}))
        end_time = time.time()
        read_times.append(end_time - start_time)
    # print(end_time - start_time)
    min = 100000
    max = -1
    sum = 0
    for i in read_times:
        if i < min:
            min = i
        if i > max:
            max = i
        sum += i
    print("min: %s, max: %s, avg: %s" % (min, max, sum/n))


def test_n_random_reads(collection, n, n_unique_random_ids, m):
    # n_unique_random_ids = random.sample(range(1, 2000000), n)
    m_print_reads = random.sample(range(1, n), m)
    # read_times = []
    j = 1
    for i in n_unique_random_ids:
        if j in m_print_reads:
            # start_time = time.time()
            # collection.find_one({get_primary_key(): i})
            print(collection.find_one({get_primary_key(): i}))
            # end_time = time.time()
            # read_times.append(end_time - start_time)
        j += 1
    # print(end_time - start_time)
    # min = 100000
    # max = -1
    # sum = 0
    # for i in read_times:
    #     if i < min:
    #         min = i
    #     if i > max:
    #         max = i
    #     sum += i
    # print("min: %s, max: %s, avg: %s" % (min, max, sum/n))


def get_primary_key():
    return "_id"


def get_list_from_file(filepath):
    ids = []
    with open(filepath, 'r') as istr:
        for i, line in enumerate(istr):
            ids.append(line.rstrip('\n'))
    return ids


if __name__ == '__main__':
    client = MongoClient('localhost',
                         27017)
    db = client["test_db"]
    test_collection = db["test"]
    test_n_reads(test_collection, 10000, get_list_from_file("ten_k_ids.txt"))
    test_n_reads(test_collection, 20000, get_list_from_file("twenty_k_ids.txt"))
    test_n_reads(test_collection, 30000, get_list_from_file("thirty_k_ids.txt"))
    test_n_reads(test_collection, 40000, get_list_from_file("forty_k_ids.txt"))
    test_n_reads(test_collection, 50000, get_list_from_file("fifty_k_ids.txt"))
    test_n_reads(test_collection, 60000, get_list_from_file("sixty_k_ids.txt"))
    test_n_reads(test_collection, 70000, get_list_from_file("seventy_k_ids.txt"))
    test_n_reads(test_collection, 80000, get_list_from_file("eighty_k_ids.txt"))
    test_n_reads(test_collection, 90000, get_list_from_file("ninety_k_ids.txt"))
    test_n_reads(test_collection, 100000, get_list_from_file("hundred_k_ids.txt"))
    test_n_random_reads(test_collection, 10000, get_list_from_file("ten_k_ids.txt"), 4)
