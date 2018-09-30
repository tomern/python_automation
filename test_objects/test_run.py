from datetime import datetime
from mongo_folder.mongo import MongoDb
from test_objects.results import Results
import time
from datetime import timedelta


class TestRun:
    def __init__(self, env):
        self.db = MongoDb("test").db
        self.col = self.db.get_collection('Runs')
        self.test_run_id = self.col.count() + 1
        self.env = env
        self.duration = None
        self.date = str(time.strftime('%d/%m/%Y %H:%M:%S'))
        self.results = Results()
        self.json = {'TestRunId': self.test_run_id,
                     'Env': self.env,
                     'Date': self.date,
                     'Results': {'passed': 0, 'failed': 0},
                     'Duration': self.duration
                     }
        self.col.replace_one(filter={'TestRunId': self.test_run_id}, replacement=self.json, upsert=True)

    def update_results(self, request):
        num_failed = request.session.testsfailed
        num_passed = request.session.testscollected - num_failed
        self.json['Results']['failed'] = num_failed
        self.json['Results']['passed'] = num_passed
        time_temp = \
            datetime.strptime(str(time.strftime('%d/%m/%Y %H:%M:%S')), '%d/%m/%Y %H:%M:%S') \
            - datetime.strptime(self.date, '%d/%m/%Y %H:%M:%S')
        self.duration = str(int(time_temp / timedelta(seconds=1)))
        self.json['Duration'] = self.duration
        self.col.replace_one(filter={'TestRunId': self.test_run_id}, replacement=self.json, upsert=True)




