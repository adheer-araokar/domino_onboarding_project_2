#!/usr/bin/env python3

from time import sleep
from latlng_producer.producer import produce

import threading


def main():

    for i in range(10):
        t = threading.Thread(target=produce)
        t.start()
        sleep(1)


if __name__ == '__main__':
    main()
