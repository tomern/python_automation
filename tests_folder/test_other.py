from configuration_folder import configuration as cfg
from helper_folder import mathlib
import requests
import pytest
from pytest import mark
from helper_folder import cloudinary as cloud
from helper_folder import cloudinary_new as cloudnew
from helper_folder import files
import datetime


@mark.smoke
class TestClass:
    @pytest.mark.skipif(2 > 2, reason="I don't want to run this now")
    def test_calc_total(self):
        res = mathlib.calc_total(6, 5)
        assert res > 10

    @pytest.mark.sanity
    def test_calc_multiply1(self):
        res = mathlib.calc_multiply(2, 6)
        assert res > 10

    @pytest.mark.sanity
    def test_calc_multiply2(self):
        res = mathlib.calc_multiply(2, 6)
        assert res > 10

    def test_request_google(self):
        r = requests.get('http://www.google.com')
        assert r.status_code == 200

    @pytest.mark.parametrize('n', [1, 2, 4, 3])
    def test_params(self, n):
        print(n)
        assert n > 0

    def test_configuration(self):
        config = cfg.number
        print(config)
        return config

    def test_cloudinary(self):
        url = cloud.upload_cloudinary('C:/Users/tomern23/Pictures/Cat.jpg')
        assert url is not None

    def test_file_open_and_write(self):
        data = str(datetime.datetime.now())
        path = "C:/Users/tomern23/PycharmProjects/PytestProject/files/test.txt"
        files.save_file(data, path)
        file = open(path)
        content = file.read()
        file.close()
        print(content)
        assert data in content

    def test_cloudinary_with_config_json(self):
        url = cloudnew.upload_cloudinary('C:/Users/tomern23/Pictures/Cat.jpg')
        assert url is not None

    def test_get_user_from_config(self):
        res = cfg.User.SiteA.usrename
        assert res is not None

    def test_print_name(self, env):
        if env == "qa":
            assert 2 > 1
        if env == "stam":
            assert 2 < 1

    @mark.config
    def test_env_is_qa(self, app_config):
        assert 'qa' in app_config.base_url

    @mark.config
    def test_env_is_dev(self, app_config):
        assert 'dev' not in app_config.base_url

    def test_api_mongo_services_get(self):
        res = requests.get('http://localhost:8216/api/testrun')
        # assert 0 <= int(res.text)
        # assert res.status_code == 200, res.text

    def test_api_mongo_services_post(self):
        req_headers = {"authorization": "Bearer token"}
        res = requests.post(url='https://httpbin.org/post', headers=req_headers, json={})
        # res = requests.post(data='https://httpbin.org/post', headers=req_headers)
        json = res.json()
        url = json['headers']['Host']
        assert url

    def test_test_name(self, request):
        assert request.node.name == 'test_test_name'

    @mark.testrun
    def test_test_run1(self, test_run):
        assert 1 == 1

    @mark.testrun
    def test_test_run2(self, test_run):
        assert 1 == 1




