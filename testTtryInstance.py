data = []
def setup_method(self):
        print('\nSetup method called')
        global data 
        data = [
            (5,5,10),
            (20,-10,-10),
            (0,0,0)
        ]
def teardown_method(self):
        print('\nTeardown method method called')
        global data
        data = []




