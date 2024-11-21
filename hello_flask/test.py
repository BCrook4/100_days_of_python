# TODO: Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args):
        result = function(*args)
        name = function.__name__
        print(f"You called {name}{args}")
        print(f"It returned: {result}")
        return result
    return wrapper

# TODO: Use the decorator 👇
@logging_decorator
def a_function(*args):
    return sum(args)


a_function(1, 2, 3)