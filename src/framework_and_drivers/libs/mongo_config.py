from pymongo import MongoClient
from settings import URL, DB_NAME


class MongoDatabase:
    def __init__(self):
        self.client = MongoClient(URL)
        self.db = self.client[DB_NAME]
