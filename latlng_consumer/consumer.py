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
                                      enable_auto_commit=True)
        self.consumer.subscribe([kafka_global_config.TOPIC])

    def consume_message(self, data_sink, host_name):
        for message in self.consumer:
            if isinstance(message.value, Message):
                car_data = message.value
                data = {"name": car_data.key, "lat": car_data.value["lat"], "lon": car_data.value["lng"]}
                data_sink.append(data)
                add_car_location(car_data, host_name)
            else:
                print("problem")


def consume(sink=None, name=None):
    consumer_internal = Consumer()
    if sink is None:
        sink = []
    if name is None:
        name = uuid.uuid4()
    consumer_internal.consume_message(sink, name)
