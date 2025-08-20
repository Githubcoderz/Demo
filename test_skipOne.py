import pytest
   
@pytest.mark.skip(reason='Functionality not implemented')
def test_funOne():
    pass
       
   



import pytest
import sys
 
#simple skip
@pytest.mark.skip(reason='Functionality not implemented')
def test_funOne():
    pass
       
#conditional skip
#@pytest.mark.skipif(condition, reason)
@pytest.mark.skipif(sys.platform != 'linux',reason='Specifically written for Linux')
def test_funTwo():
    pass






#test to skip the whole class
import pytest
 
@pytest.mark.skip(reason='Trying to skip the whole class')
class TestClass:
    def test_One(self):
        print('test_One() from TestClass... ')
 
    def test_Two(self):
        print('test_Two() from TestClass... ')
 
    def test_Three(self):
        print('test_Three() from TestClass... ')
 






#test skip whole module
import pytest
@pytest.skip(reason='Trying to skip', allow_module_level=True)
 
 
def test_funModOne():
    print('funModOne()... called')
    assert True
 
def test_funModTwo():
    print('funModTwo()... called')
    assert True
 
def test_funModThree():
    print('funModThree()... called')
    assert True
 
 