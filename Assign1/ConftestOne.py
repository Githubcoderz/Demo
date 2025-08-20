import pytest

def pytest_addoption(parser):
    parser.addoption("--env", action="store", help="Environment: staging/dev/prod")
    parser.addoption("--exam", action="store", help="Exam type: alpha/beta/unit/module/integration")
    parser.addoption("--platform", action="store", help="Platform: Linux/Windows/MacOS")
    parser.addoption("--prot", action="store", help="Protocol: https/sftp/ssh")
    parser.addoption("--loc", action="store", help="Location: chennai/bangalore/kolkota")
    parser.addoption("--prods", action="store", help="Product: dell/lenovo/hp")

@pytest.fixture
def env(request):
    return request.config.getoption("--env")

@pytest.fixture
def exam(request):
    return request.config.getoption("--exam")

@pytest.fixture
def platform(request):
    return request.config.getoption("--platform")

@pytest.fixture
def prot(request):
    return request.config.getoption("--prot")

@pytest.fixture
def loc(request):
    return request.config.getoption("--loc")

@pytest.fixture
def prods(request):
    return request.config.getoption("--prods")