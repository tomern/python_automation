import pytest
from selenium import webdriver
import time
from mongo_folder import mongo
from pymongo import MongoClient
import unittest


# @pytest.fixture()
# def browser():
#     print("setting up...")
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.implicitly_wait(30)
#     driver.set_page_load_timeout(30)
#     yield driver
#     driver.close()
#     print("finishing...")


# @pytest.fixture
# def mongo_conn():
#     client = MongoClient()
#     db = client.configuration_folder
#     return db


# @pytest.mark.element
# def test_one(browser):
#     browser.get("https://www.google.com")
#     el = browser.find_element_by_id("lst-ib")
#     el.send_keys("Tomerdsfasdfasdfasdfasdfasdf")
#     time.sleep(3)


# @pytest.mark.mongo
# def test_two(browser):
#     browser.get("https://www.google.com")

@pytest.fixture()
def get_config():
    client = MongoClient()
    db = client.configurations
    return db


def test_configurations():
    assert 2 > 1

