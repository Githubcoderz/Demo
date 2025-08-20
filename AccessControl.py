user = {}
def requireAdmin(func):
    def wrapper(*args, **kwargs):
        if user.get('role') == 'admin':
            return func(*args, **kwargs)
        else:
            print("Access Denied")
    return wrapper

@requireAdmin
def deleteUser(userId):
    print(f"User {userId} deleted")

# Test Case 1: Admin
user = {'username': 'Ramlinga Raju', 'role': 'admin'}
deleteUser(100)  

# Test Case 2: Not Admin
user = {'username': 'Bantu Reddy', 'role': 'user'}
deleteUser(200)  