from pytest import fixture
from functools import reduce

@fixture(scope='class')
def sampleData():
    print('setup class scoped...')
    yield [1,2,3]
    print('teardown class scoped...')

class TestClassOne:
    def test_one(self, sampleData):
        print('\ntestone()...')
        assert sum(sampleData)==6

    def test_two(self, sampleData):
        print('\ntesttwo()...')
        assert reduce(lambda x,y : x * y, sampleData) ==6