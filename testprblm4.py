import pytest
@pytest.fixture
def dbConnection():
    return "MockDBConnection"

def test_db_connection(dbConnection):
    assert dbConnection is not None