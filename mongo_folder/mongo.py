from pymongo import MongoClient


class MongoDb:
    def __init__(self, db):
        self.client = MongoClient()
        self.db = self.client[db]
