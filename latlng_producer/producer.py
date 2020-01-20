from time import sleep

from kafka import KafkaProducer
from config import kafka_global_config
from message.base_message import Message
from message.lat_lng_message import LatLngMessage
from utils import serialize_message
from random import randint, seed, uniform


class Producer:

    def __init__(self):
        self.producer = KafkaProducer(bootstrap_servers=kafka_global_config.KAFKA_HOST,
                                      value_serializer=serialize_message)

    def get_producer(self):
        return self.producer

    def send_message(self, message: Message):
        self.get_producer().send(kafka_global_config.TOPIC, key=message.key.encode('utf-8'), value=message)
        self.get_producer().flush()


def produce():
    producer_internal = Producer()
    seed(1)
    # while True:
    for i in range(100):
        car_num = randint(0, 9)
        key = 'car-' + str(car_num)
        lat = round(uniform(-90, 90), 6)
        lng = round(uniform(-180, 180), 6)
        message = LatLngMessage(key, lat=lat, lng=lng)
        producer_internal.send_message(message)
        sleep(2)
