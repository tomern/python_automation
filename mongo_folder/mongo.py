from pymongo import MongoClient


class MongoDb:
    def __init__(self, db):
        self.client = MongoClient()
        self.db = self.client[db]

    def create_collection(self, col_name):
        self.db.create_collection(col_name)
