import os

DEBUG = True
HOST = '0.0.0.0'
PORT = 5000

MONGO_URI = os.getenv('MONGO_URI')
POSTGRES_URI = os.getenv('POSTGRES_URI')
