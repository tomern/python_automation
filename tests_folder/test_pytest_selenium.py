from time import sleep


def test_example1(selenium):
    selenium.get('http://www.example.com')
    for i in range(10):
        print('test_example1 step{0}'.format(i))
        sleep(1)


def test_example2(selenium):
    selenium.get('http://www.example.com')
    for i in range(10):
        print('test_example2 step{0}'.format(i))
        sleep(1)
    assert 2 == 1
