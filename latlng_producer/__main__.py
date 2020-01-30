#!/usr/bin/env python3

from time import sleep

from db.db import setup_schema
from latlng_producer.producer import produce

import threading


def main():

    setup_schema()
    for i in range(10):
        t = threading.Thread(target=produce)
        t.start()
        sleep(1)


if __name__ == '__main__':
    main()
