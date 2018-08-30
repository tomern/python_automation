import pytest
from mongo_folder.mongo import MongoDb


@pytest.fixture()
def get_db_config():
    return MongoDb("configurations").db


@pytest.fixture()
def get_db_test():
    return MongoDb("test").db


def test_configurations(get_db_config):
    db = get_db_config
    col = db.get_collection('Qa')
    doc1 = col.find_one({"Users.Reg1.UserName": "tomernoy1@gmail.com"})
    col = db.get_collection('Uat')
    doc2 = col.find_one({"Users.Reg1.UserName": "tomernoy1@gmail.com"})
    assert doc1 is not None
    assert doc2 is not None


def test_runs(get_db_test):
    db = get_db_test
    col = db.get_collection('Runs')
    doc = col.find_one({"TestRunId": "1"})
    assert doc is not None



