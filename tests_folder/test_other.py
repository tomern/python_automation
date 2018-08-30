from configuration_folder import configuration
from helper_folder import mathlib
import requests
import pytest


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
        config = configuration.Configurations.number
        print(config)
        return config


