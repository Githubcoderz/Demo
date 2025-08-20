from pytest import fixture
from functools import reduce
 
@fixture(params=[(1,2,3), (3,2, 1)])
def sampleData(request):
    print('setup class scoped...')
    yield request.param
    print('teardown class scoped...')
 
class TestClassOne:
    def test_One(self, sampleData):
        print(f'\ntestOne()...with {sampleData}')
        assert sum(sampleData) == 6
 
    def test_Two(self, sampleData):
        print(f'\ntestTwo()...with {sampleData}')
        assert reduce(lambda x, y: x * y, sampleData) == 6
    print('*' * 40)
 
#multiple Parameters
from pytest import fixture
from functools import reduce
 
@fixture(params=[([1,2,3], 6), ([3,2, 1], 6), ([2, 3, 5], 10)])
def sampleData(request):
    print('\nsetup class scoped...')
    yield request.param
    print('teardown class scoped...')
    print('*' * 40)
 
class TestClassOne:
    def test_One(self, sampleData):
        col, res = sampleData
        print(f'\ntestOne()...with col: {col} and res: {res}')
        assert sum(col) == res
 
 