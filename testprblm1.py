def setup_function():
    global dbConnection
    dbConnection = "TestDBConnection"

def test_connection_is_not_none():
    assert dbConnection is not None


