from parse_rest.connection import register
from parse_rest.user import User


APPLICATION_ID = ""
REST_API_KEY = ""

register(APPLICATION_ID, REST_API_KEY)


def singup(user_name, password):
    return User.signup(user_name, password)


def login(user_name, password):
    return User.login(user_name, password)
