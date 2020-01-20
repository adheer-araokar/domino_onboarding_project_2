import jsonpickle
import simplejson as json

from message.base_message import Message


def serialize_message(message: Message):
    return jsonpickle.encode(message).encode('utf-8')
    # return json.dumps(message, cls=MessageEncoder)


def deserialize_message(json_str):
    return jsonpickle.decode(json_str.decode('utf-8'))
    # return json.load(json_str, object_hook=Message)


# class MessageEncoder(json.JSONEncoder):
#
#     def default(self, o):
#         return {'__{}__'.format(o.__class__.__name__): o.__dict__}
