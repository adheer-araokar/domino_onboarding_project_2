from kafka import KafkaConsumer
from config import kafka_global_config
from db.db import get_mongo_client, add_car_location
from message.base_message import Message
import uuid
from utils import deserialize_message

mongo_db_client = get_mongo_client()


class Consumer:

    def __init__(self):
        self.consumer = KafkaConsumer(bootstrap_servers=kafka_global_config.KAFKA_HOST,
                                      value_deserializer=deserialize_message,
                                      group_id='same_grp',
                                      # auto_offset_reset='earliest',
                                      enable_auto_commit=False)
        self.consumer.subscribe([kafka_global_config.TOPIC])

    def consume_message(self):
        for message in self.consumer:
            if isinstance(message.value, Message):
                car_data = message.value
                add_car_location(car_data)
                self.consumer.commit()
            else:
                print("problem")


def consume():
    consumer_internal = Consumer()
    consumer_internal.consume_message()
