import pytest

@pytest.fixture
def username():
    return "admin"

@pytest.fixture
def userProfile(username):
    return {
        "user": username,
        "role": "admin"
    }
def profile(userProfile):
    assert userProfile["user"] == "admin"
    assert userProfile["role"] == "admin"