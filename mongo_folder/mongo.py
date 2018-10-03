from pymongo import MongoClient


class MongoDb:
    def __init__(self, db):
        self.client = MongoClient()
        self.db = self.client[db]

    def create_collection(self, col_name):
        self.db.create_collection(col_name)

    def update_steps(self, step, test):
        test.steps.append(step)
        # col = self.db.get_collection(f'testRun{test.test_run_id}')
        col = self.db.get_collection("testRun{0}".format(test.test_run_id))
        col.update_one(filter={'TestNumber': test.test_number}, update={"$set": {"address": "Canyon 123"}})
