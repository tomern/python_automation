from helper_folder import mathlib
import requests
import pytest
from pytest import mark
from helper_folder import cloudinary as cloud
from helper_folder import cloudinary_new as cloudnew
from helper_folder import files
import datetime
from configuration_folder import my_config as cfg
import redis


@pytest.mark.skipif(2 > 2, reason="I don't want to run this now")
def test_calc_total(test_run):
    res = mathlib.calc_total(6, 5)
    assert res > 10


@pytest.mark.sanity
def test_calc_multiply1(test_run):
    res = mathlib.calc_multiply(2, 6)
    assert res > 10


@pytest.mark.sanity
def test_calc_multiply2(test_run):
    res = mathlib.calc_multiply(2, 6)
    assert res > 10


def test_request_google(test_run):
    r = requests.get('http://www.google.com')
    assert r.status_code == 200


@pytest.mark.parametrize('n', [1, 2, 4, 3])
def test_params(n, test_run):
    print(n)
    assert n > 0


def test_configuration(test_run):
    config = cfg.number
    print(config)
    return config


def test_cloudinary(test_run, app_config):
    url = cloud.upload_cloudinary(app_config.image, app_config)
    assert url is not None


def test_file_open_and_write(test_run):
    data = str(datetime.datetime.now())
    path = "C:/Users/tomern23/PycharmProjects/PytestProject/files/test.txt"
    files.save_file(data, path)
    file = open(path)
    content = file.read()
    file.close()
    print(content)
    assert data in content


def test_cloudinary_with_config_json(test_run, app_config):
    url = cloudnew.upload_cloudinary(app_config.image)
    assert url is not None


def test_print_name(env, test_run):
    if env == "qa":
        assert 2 > 1
    if env == "stam":
        assert 2 < 1


@mark.config
def test_env_is_qa(app_config, test_run):
    assert 'qa' in app_config.base_url


@mark.config
def test_env_is_dev(app_config, test_run):
    assert 'dev' not in app_config.base_url


def test_api_mongo_services_get(test_run):
    res = requests.get('http://mongo_services:8216/api/Configurations/Qa')
    assert res.status_code == 200, res.text


def test_api_mongo_services_post(test_run, app_config):
    req_headers = {"authorization": "Bearer token"}
    res = requests.post(url='{0}/post'.format(app_config.urls['service_url']), headers=req_headers, json={})
    # res = requests.post(data='https://httpbin.org/post', headers=req_headers)
    json = res.json()
    url = json['headers']['Host']
    assert url


def test_test_name(request, test_run):
    assert request.node.name == 'test_test_name'


@mark.testrun
def test_test_run1(app_config, test_run, test, get_db_test, request):
    assert 1 == 1


@mark.testrun
def test_test_run2(app_config, test_run, test, get_db_test, request):
    assert 1 == 1


def test_lambda():
    list1 = []
    list2 = []
    list1.append("a")
    list1.append("b")
    list1.append("c")
    # Like Where lambda in C#
    res = [l for l in list1 if l == "a" or l == "b"]
    # Like ForEach lambda in C#
    for i in list1: list2.append(i)
    assert len(res) == 2
    assert list1 == list2


def test_redis():
    r = redis.StrictRedis(host='redis', decode_responses=True)
    # r.set("key1", "value1")
    res = r.get("key1")
    print(res)
    assert "value1" == res, 'verify value of key'
