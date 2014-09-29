import socket
from datetime import datetime
from .backends import parse


class User:
    user = None

    @classmethod
    def login(cls, user_name, password):
        try:
            cls.user = parse.login(user_name, password)
        except Exception as error:
            print(error)

    @classmethod
    def copy_to_cloud(cls, value):
        if cls.user:
            cls.user.clipboard.append({'value': value,
                                       'time': str(datetime.now()),
                                       'host': socket.gethostname()})
            cls.user.save()

    @classmethod
    def get_from_cloud(cls):
        if cls.user:
            history = cls.user.clipboard
            if history:
                return history[-1]['value']
            else:
                return []

    @classmethod
    def get_history(cls):
        return cls.user.clipboard

    @classmethod
    def wipe(cls):
        cls.user.clipboard = []
        cls.user.save()
