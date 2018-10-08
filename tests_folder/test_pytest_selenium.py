from time import sleep


def test_example1(selenium):
    selenium.get('http://www.example.com')
    sleep(5)


def test_example2(selenium):
    selenium.get('http://www.example.com')
    sleep(5)
    assert 2 == 1
