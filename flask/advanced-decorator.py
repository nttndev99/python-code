from functools import wraps
##-------------------------- Advanced Python Decorator Functions
class User: # Class User
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(function): # Decorator
    @wraps(function)
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
        else:
            print("User is not authenticated.")   
    return wrapper

@is_authenticated_decorator
def create_blog_post(user): # Decorated Function
    print(f"This is {user.name}'s new blog post.")

# Test
new_user = User("angela")
new_user.is_logged_in = True
create_blog_post(new_user)

# Test metadata
# print(create_blog_post.__name__)  
# print(create_blog_post.__doc__)    
# print(create_blog_post.__module__) 




##-------------------------- Create the logging_decorator() function 
from functools import wraps

def logging_decorator(func):
    @wraps(func)
    def wrapper(*args):
        # Print function call with arguments
        print(f"You called {func.__name__}{args}")
        # Call the original function
        result = func(*args)
        # Print the returned result
        print(f"It returned: {result}")
        return result
    return wrapper

# Use the decorator 
@logging_decorator
def a_function(*args):
    return sum(args)
    
a_function(1,2,3)