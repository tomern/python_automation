from test_objects.test_run import TestRun
import random as rnd


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


def test_create_collection(get_db_test):
    db = get_db_test
    col_to_create = "stam{0}".format(str(rnd.Random().randint(100, 200)))
    # col_to_create = f"stam{str(rnd.Random().randint(100, 200))}"
    db.create_collection(name=col_to_create)
    print(db.list_collection_names())
    assert col_to_create in db.list_collection_names()


def test_insert_test_run(get_db_test, env):
    test_run = TestRun(env)

