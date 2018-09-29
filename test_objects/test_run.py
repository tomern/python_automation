from mongo_folder.mongo import MongoDb
import time


class TestRun:
    def __init__(self, env):
        self.db = MongoDb("test").db
        self.col = self.db.get_collection('Runs')
        self.test_run_id = self.col.count() + 1
        self.env = env
        self.date = str(time.strftime('%d/%m/%Y %H:%M:%S'))
        json = {'TestRunId': self.test_run_id, 'Env': self.env, 'Date': self.date}
        self.col.replace_one(filter={'TestRunId': self.test_run_id}, replacement=json, upsert=True)






