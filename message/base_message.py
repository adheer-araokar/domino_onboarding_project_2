

class Message(object):

    def __init__(self, key: str = None, value: dict = None):
        self._key = key
        self._value = value

    @property
    def key(self) -> str:
        return self._key

    @key.setter
    def key(self, key: str):
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")

        self._key = key

    @property
    def value(self) -> dict:
        return self._value

    @value.setter
    def value(self, value: dict):
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")

        self._value = value
