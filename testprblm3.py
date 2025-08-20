
userProfile = []

def setup_function():
    global userProfile
    username = "Admin" 
    userProfile = {'user': username, 'role': 'admin'}
    print("\nSetup: userProfile initialized.")

def teardown_function():
    global userProfile
    userProfile = []
    print("Teardown: userProfile cleared.")

def test_user_profile_values():
    assert userProfile['user'] == "Admin"
    assert userProfile['role'] == "admin"