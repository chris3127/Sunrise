import os

class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY') or 'this-is-my-secret-key'