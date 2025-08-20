data= []
def setup_module():
    print('\nsetup module called before any tests')
    global data
    data = [
        (3,5,8)
        (10,-20,-10)
        (0,0,0)    
    ]
def teardown_module():
    print('\ntearup module called after all tests')
    global data 
    data = []
def test_funOne():
    print('running funOne')
    
 
def test_funTwo():
    print('\nrunning funTwo')
    assert True
 
def test_funThree():
    print('\nrunning funThree')
    assert True
 