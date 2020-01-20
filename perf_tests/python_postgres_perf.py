import psycopg2
import time

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


# conn = psycopg2.connect("dbname=test_db")
conn = psycopg2.connect(host="127.0.0.1",
                        port="5432",
                        database="test_db")
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT);
cur = conn.cursor()


def setup_schema():
    create_table_query = get_create_table_query()
    cur.execute(create_table_query)


def get_create_table_query():
    query = 'CREATE TABLE test (ID SERIAL PRIMARY KEY, '
    for i in range(101):
        if i == 100:
            query += "key" + str(i) + " TEXT NOT NULL);"
        else:
            query += "key" + str(i) + " TEXT NOT NULL, "
    return query


def get_insert_row_statement():
    query = 'INSERT INTO test('
    for i in range(101):
        if i == 100:
            query += "key" + str(i) + ") VALUES ("
        else:
            query += "key" + str(i) + ", "
    for i in range(101):
        if i == 100:
            query += "%s" + ");"
        else:
            query += "%s" + ", "

    values = []
    for i in range(101):
        val = 'val' + str(i)
        values.append(str(val))
    return query, tuple(values)


def test_insert():

    start_time = time.time()

    for i in range(1000000):
        insert_row_statement, values = get_insert_row_statement()
        cur.execute(insert_row_statement, values)


    end_time = time.time()

    print(end_time - start_time)


def test_read():
    start_time = time.time()
    fetch_row_statement, values = get_fetch_query()
    cur.execute(fetch_row_statement, values)
    print(cur.fetchall())
    end_time = time.time()
    print(end_time - start_time)


def get_fetch_query():
    return 'SELECT * FROM test WHERE key78 = %s;', tuple(['val78'])

#
#
# def test_read():
#     start_time = time.time()
#     test_collection.find_one({"key9999": "value9999"})
#     end_time = time.time()
#     print(end_time - start_time)
#
#

#
#

#
#
if __name__ == '__main__':
    # setup_schema()
    # test_insert()
    test_read()
    conn.close()


