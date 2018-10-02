from mongo_folder.mongo import MongoDb
from datetime import datetime
import time


class Test:
    def __init__(self, test_run, request):
        self.timef = '%d/%m/%Y %H:%M:%S'
        self.db = MongoDb("test").db
        self.test_run_id = test_run.test_run_id
        self.col = self.db.get_collection(f'testRun{self.test_run_id}')
        self.result = {
                        'Status': '',
                        'StackTrace': '',
                        'ErrorMessage': '',
                        'ScreenShot': '',
                        'Url': ''
                        }
        self.test_name = request.node.name
        self.steps = []
        self.env = test_run.env
        self.date = str(time.strftime(self.timef))
        self.duration = None
        self.video = ''
        self.session_id = ''
        self.json = {
                     'TestName': self.test_name,
                     'Steps': self.steps,
                     'Result': self.result,
                     'TestRunId': self.test_run_id,
                     'Date': self.date,
                     'Env': self.env,
                     'Duration': self.duration,
                     'Video': self.video,
                     'SessionId': self.session_id
                     }
        self.col.replace_one(filter={'TestName': self.test_name}, replacement=self.json, upsert=True)

    def update_results(self):
        self.duration = str(datetime.strptime(str(time.strftime(self.timef)), self.timef)
                            - datetime.strptime(self.date, self.timef)
                            )
        self.json['Duration'] = self.duration
        self.col.replace_one(filter={'TestName': self.test_name}, replacement=self.json, upsert=True)
