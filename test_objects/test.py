from mongo_folder.mongo import MongoDb


class Test:
    def __init__(self, env):
        self.db = MongoDb("test").db

