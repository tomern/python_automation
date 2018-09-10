from configuration_folder import configuration as cfg
from helper_folder import mathlib
import requests
import pytest
from helper_folder import cloudinary as cloud
from helper_folder import cloudinary_new as cloudnew
from helper_folder import files
import datetime


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

    @pytest.mark.parametrize('n', [1, 2, 4])
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

    def test_get_usre_from_config(self):
        res = cfg.User.SiteA.usrename
        assert res is not None


