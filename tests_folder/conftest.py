

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="qa")


def pytest_generate_tests(metafunc):
    option_value = metafunc.config.option.env
    if 'env' in metafunc.fixturenames and option_value is not None:
        metafunc.parametrize("env", [option_value])
