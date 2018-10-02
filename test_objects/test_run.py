from datetime import datetime
from mongo_folder.mongo import MongoDb
from test_objects.results import Results
import time


class TestRun:
    def __init__(self, env):
        self.db = MongoDb("test").db
        self.col = self.db.get_collection('Runs')
        self.test_run_id = self.col.count() + 1
        self.env = env
        self.duration = None
        self.timef = '%d/%m/%Y %H:%M:%S'
        self.date = str(time.strftime(self.timef))
        self.results = Results()
        self.json = {'TestRunId': self.test_run_id,
                     'Env': self.env,
                     'Date': self.date,
                     'Results': {'Passed': 0, 'Failed': 0, 'SentToHub': 0, 'Running': 0},
                     'Duration': self.duration
                     }
        self.col.replace_one(filter={'TestRunId': self.test_run_id}, replacement=self.json, upsert=True)

    def update_results(self, request):
        self.duration = str(datetime.strptime(str(time.strftime(self.timef)), self.timef)
                            - datetime.strptime(self.date, self.timef)
                            )
        self.json['Duration'] = self.duration
        self.json['Results']['Failed'] = request.session.testsfailed
        self.json['Results']['Passed'] = request.session.testscollected - request.session.testsfailed
        self.col.replace_one(filter={'TestRunId': self.test_run_id}, replacement=self.json, upsert=True)



