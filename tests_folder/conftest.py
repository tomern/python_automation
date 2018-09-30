from pytest import fixture
from mongo_folder.mongo import MongoDb
from browser_folder.browser import Browser
from configuration_folder import my_config
from test_objects.test_run import  TestRun


# adding env param from cmd
def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="qa", help="environment to run tests")


# config fixture
@fixture(scope='session')
def app_config(env):
    cfg = my_config.Config(env)
    return cfg


# env fixture env
@fixture(scope='session')
def env(request):
    return request.config.getoption("--env")


# configuration from MongoDB fixture
@fixture()
def get_db_config():
    return MongoDb("configurations").db


# test object from MongoDB fixture
@fixture()
def get_db_test():
    return MongoDb("test").db


# Browser fixture
@fixture()
def browser():
    _browser = Browser()
    yield _browser
    _browser.quit()


# Creating a fixture that creates a testrun
@fixture(scope='session')
def test_run(env, request):
    testrun = TestRun(env)
    yield testrun
    testrun.update_results(request)


@fixture()
def stam(request):
    return request


