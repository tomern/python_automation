from time import sleep


def test_example1(selenium):
    selenium.get('http://www.example.com')
    # sleep(15)


def test_example2(selenium):
    selenium.get('http://www.example.com')
    # sleep(15)
    assert 2 == 1
