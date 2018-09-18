from pytest import fixture
from mongo_folder.mongo import MongoDb
from browser_folder.browser import Browser


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="qa")


def pytest_generate_tests(metafunc):
    option_value = metafunc.config.option.env
    if 'env' in metafunc.fixturenames and option_value is not None:
        metafunc.parametrize("env", [option_value])


@fixture()
def get_db_config():
    return MongoDb("configurations").db


@fixture()
def get_db_test():
    return MongoDb("test").db


@fixture()
def browser():
    _browser = Browser()
    yield _browser
    _browser.quit()
