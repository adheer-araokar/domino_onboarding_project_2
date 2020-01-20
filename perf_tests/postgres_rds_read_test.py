import psycopg2
import time
import random

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def test_n_reads(cursor, n, n_unique_random_ids):
    # n_unique_random_ids = random.sample(range(1, 2000000), n)
    read_times = []
    for i in n_unique_random_ids:
        start_time = time.time()
        fetch_row_statement, values = get_fetch_query(i)
        cursor.execute(fetch_row_statement, values)
        cursor.fetchall()
        # print(cursor.fetchall())
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


def test_n_random_reads(cursor, n, n_unique_random_ids, m):
    # n_unique_random_ids = random.sample(range(1, 2000000), n)
    m_print_reads = random.sample(range(1, n), m)
    # read_times = []
    j = 1
    for i in n_unique_random_ids:
        if j in m_print_reads:
            # start_time = time.time()
            fetch_row_statement, values = get_fetch_query(i)
            cursor.execute(fetch_row_statement, values)
            # cursor.fetchall()
            print(cursor.fetchall())
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


def get_table_name():
    return 'test'


def get_table_primary_key():
    return '_id'


def get_fetch_query(val):
    return 'SELECT * FROM ' + get_table_name() + ' WHERE ' + get_table_primary_key() + ' = %s;', tuple([val])


def get_list_from_file(filepath):
    ids = []
    with open(filepath, 'r') as istr:
        for i, line in enumerate(istr):
            ids.append(line.rstrip('\n'))
    return ids


if __name__ == '__main__':
    conn = psycopg2.connect(host="database-1.cv22shqrmfki.us-east-2.rds.amazonaws.com",
                            port="5432",
                            database="test_db",
                            user="postgres",
                            password="postgres123")
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()
    # test_n_reads(cursor, 10000, get_list_from_file("ten_k_ids.txt"))
    # test_n_reads(cursor, 20000, get_list_from_file("twenty_k_ids.txt"))
    # test_n_reads(cursor, 30000, get_list_from_file("thirty_k_ids.txt"))
    # test_n_reads(cursor, 40000, get_list_from_file("forty_k_ids.txt"))
    # test_n_reads(cursor, 50000, get_list_from_file("fifty_k_ids.txt"))
    # test_n_reads(cursor, 60000, get_list_from_file("sixty_k_ids.txt"))
    # test_n_reads(cursor, 70000, get_list_from_file("seventy_k_ids.txt"))
    # test_n_reads(cursor, 80000, get_list_from_file("eighty_k_ids.txt"))
    # test_n_reads(cursor, 90000, get_list_from_file("ninety_k_ids.txt"))
    # test_n_reads(cursor, 100000, get_list_from_file("hundred_k_ids.txt"))
    test_n_random_reads(cursor, 10000, get_list_from_file("ten_k_ids.txt"), 4)
    conn.close()
