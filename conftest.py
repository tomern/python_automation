from pytest import fixture
from selenium.webdriver.support.wait import WebDriverWait
from mongo_folder.mongo import MongoDb
from browser_folder.browser import Browser
from configuration_folder import my_config
from test_objects.testrun import Run
from test_objects.test import Test
import os
# import mysql.connector


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


# mysql container fixture
@fixture(scope='session')
def my_sql(app_config):
    sql = app_config.connections['sql_container']
    my_host = sql['host'] if app_config.local else 'mysql'
    mydb = mysql.connector.connect(
        host=my_host,
        port=sql['port'],
        user=sql['user'],
        password=sql['password'],
    )
    yield mydb
    mydb.close()


# configuration from MongoDB fixture
@fixture()
def get_db_config(app_config):
    return MongoDb("configurations", app_config).db


# test object from MongoDB fixture
@fixture()
def get_db_test(app_config):
    return MongoDb("test", app_config).db


# browser fixture
@fixture()
def browser(app_config, request):
    _browser = Browser(app_config, request)
    yield _browser
    _browser.quit()


# TestRun fixture
@fixture(scope='session')
def test_run(app_config, request):
    testrun = Run(app_config)
    yield testrun
    testrun.update_results(request)


# Test fixture
@fixture()
def test(test_run, request, app_config):
    test = Test(test_run, request, app_config)
    yield test
    test.update_results()


# Request fixture
@fixture()
def stam(request):
    return request


@fixture
def selenium(selenium):
    # selenium.implicitly_wait(10)
    selenium.wait_until = lambda func, time_out=10: WebDriverWait(selenium, time_out).until(func)
    selenium.wait_until_not = lambda func, time_out=10: WebDriverWait(selenium, time_out).until_not(func)
    try:
        selenium.maximize_window()
    except:
        pass
    return selenium


@fixture(scope='session')
def session_capabilities(session_capabilities):
    session_capabilities['enableVNC'] = True
    session_capabilities['enableVideo'] = True
    session_capabilities['name'] = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
    return session_capabilities
