from functools import wraps

def max_result(threshold):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)    
            if result > threshold:
                print(f"Results is too big ({result}). "
                      f"Max allowed is {threshold}")
            return result
        return wrapper
    return decorator
    
@max_result(75)
def cube(n):
    return n**3

print(cube(5))
        