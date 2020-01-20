from kafka import SimpleClient
from config import kafka_global_config

kafka_client = SimpleClient(kafka_global_config.KAFKA_HOST)


def get_topics():
    return kafka_client.topics


class CarPartitioner(object):

    @classmethod
    def __call__(cls, key, all_partitions, available):

        if key is None:
            raise Exception("All records must have a key in the format car-{car_num}")

        idx = key.split('-')[1]
        return all_partitions[idx]
