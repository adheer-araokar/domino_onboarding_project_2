from message.base_message import Message


class LatLngMessage(Message):

    def __init__(self, key: str, lat: float, lng: float):
        value = {"lat": lat, "lng": lng}
        super().__init__(key, value)
