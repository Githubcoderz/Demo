data = []
class TestTryClass:
    @classmethod
    def setup_class(cls):
        print('\nSetup class method called')
        global data 
        data = [
            (5,5,10),
            (20,-10,-10)
        ]
    @classmethod
    def teardown_class(cls):
        print('\nTeardown class method called')
        global data
        data=[]

    def test_add(cls):
        print('\nAdd method called')
        for x,y , res in cls.test_addData:
            assert x + y == res

